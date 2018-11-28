// B_Revenge_of_the_Pancakes.cpp : main project file.

#include "stdafx.h"

using namespace System;

System::Int32 RunTest (System::String^ str);

int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        System::Int32 result = RunTest(rdr->ReadLine());
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
        System::Console::WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
    }
    rdr->Close();
    wtr->Close();
    return 0;
}

#define MIN(a,b) ((a)<(b)?(a):(b))
System::String^ flip (System::String^ str, System::Int32 flip, System::Int32 total);
System::Int32 RunTest (System::String^ str)
{
    System::Int32 retval = 0;
    System::Int32 back = str->Length;
    while (back)
    {
        for (back = str->Length; ((back>0) && (str[back-1] == '+')); back--);
        str = str->Substring(0,back);
        // count '+' from the front
        System::Int32 frontPlus = 0;
        while ((frontPlus < back) && (str[frontPlus] == '+'))
            frontPlus++;
        // count '-' from the back
        System::Int32 backMinus = str->Length;
        while ((backMinus > 0) && (str[backMinus-1] == '-'))
            backMinus--;
        System::Int32 flipVal = MIN(frontPlus, backMinus);
        if (flipVal)
        {
            str = flip (str, flipVal, str->Length);
            retval++;
        }
        if (frontPlus < str->Length)
        {
            str = flip (str, str->Length, str->Length);
            retval++;
        }
    }
    return retval;
}

System::String^ flip (System::String^ str, System::Int32 flip, System::Int32 total)
{
    System::String^ retval;
    System::Int32 i;
    for (i=0; i<flip; i++)
    {
        retval += str[flip-i-1]=='+'?"-":"+";
    }
    if (flip < total) retval += str->Substring(flip,total-flip);
    return retval;
}