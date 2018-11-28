// C_Dijkstra.cpp : main project file.

#include "stdafx.h"

using namespace System;

enum OneIJK
{
    One,
    I,
    J,
    K
};

struct ElementType
{
    char        neg;
    enum OneIJK v;
};
// ijk = -1
const struct ElementType Mult[4][4] =
{
    {{0,One}, {0,  I}, {0,  J}, {0,  K}},
    {{0,  I}, {1,One}, {0,  K}, {1,  J}},
    {{0,  J}, {1,  K}, {1,One}, {0,  I}},
    {{0,  K}, {0,  J}, {1,  I}, {1,One}}
};

enum OneIJK ToEnum(System::Char c)
{
    return c=='1'?One:
           c=='i'?I:
           c=='j'?J:K;
}

System::Int32 ToIdx(enum OneIJK e)
{
    return e==One?0:
           e==I?1:
           e==J?2:3;
}
System::Int32 Build (System::String^ t, enum OneIJK e)
{
    System::Int32 retval = -1;
    struct ElementType c = {false, One};
    System::Int32 i=0;
    while ((retval == -1) && (i<t->Length))
    {
        enum OneIJK conv = ToEnum(t[i]);
        struct ElementType m = Mult[ToIdx(c.v)][ToIdx(conv)];
        c.neg ^= m.neg;
        c.v = m.v;
        i++;
        if (c.v == e && c.neg == false)
        {
            switch (c.v)
            {
            case I:
                //Console::WriteLine ("i = " + t->Substring(0,i));
                retval = Build (t->Substring(i), J);
                break;
            case J:
                //Console::WriteLine ("j = " + t->Substring(0,i));
                retval = Build (t->Substring(i), K);
                break;
            case K:
                if (i < t->Length) retval = -1;
                else
                {
                    //Console::WriteLine ("k = " + t->Substring(0,i));
                    retval = 0;
                }
                break;
            }
        }
    }
    return retval;
}

System::Boolean RunTest (System::String^ t)
{
    //System::Int32 Result = Build(t, I);
    //return (Result==0)?true:false;
    struct ElementType c = {false, One};
    System::Int32 progress = 0;
    for each (System::Char ch in t)
    {
        enum OneIJK conv = ToEnum(ch);
        struct ElementType m = Mult[ToIdx(c.v)][ToIdx(conv)];
        c.neg ^= m.neg;
        c.v = m.v;
        if (c.neg == false)
        {
            switch (progress)
            {
            case 0: // looking for i
                if (c.v == I) progress++;
                break;
            case 1: // looking for ij = k
                if (c.v == K) progress++;
                break;
            }
        }
    }
    //looking for ijk = -1
    return (progress == 2) && c.neg && (c.v == One);
}

System::Boolean RunTest (System::String^ t, System::Int64 repeat)
{
    struct ElementType c = {false, One};
    System::Int32 progress = 0;
    while (repeat > 0)
    {
        for each (System::Char ch in t)
        {
            enum OneIJK conv = ToEnum(ch);
            struct ElementType m = Mult[ToIdx(c.v)][ToIdx(conv)];
            c.neg ^= m.neg;
            c.v = m.v;
            if (c.neg == false)
            {
                switch (progress)
                {
                case 0: // looking for i
                    if (c.v == I) progress++;
                    break;
                case 1: // looking for ij = k
                    if (c.v == K) progress++;
                    break;
                }
            }
        }
        repeat--;
        if (progress == 2)
        {
            repeat &= 3;
        }
    }
    //looking for ijk = -1
    return (progress == 2) && c.neg && (c.v == One);
}


int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        System::String^ line = rdr->ReadLine();
        array<System::String^>^ split = line->Split();
        System::Int64 repeat = System::Convert::ToInt64 (split[1]);
        line = rdr->ReadLine();
        System::String^ Test = "";
        //for (System::Int32 j=0; j<repeat; j++)
        //{
        //   Test += line;
        //}
        System::Console::WriteLine ("Case #" + (i+1).ToString());
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+(RunTest(line, repeat&127)?"YES":"NO"));
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
