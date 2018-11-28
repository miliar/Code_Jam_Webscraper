// A_Mushroom.cpp : main project file.

#include "stdafx.h"

using namespace System;
System::String^ RunTest (System::String^ t);

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
        line = rdr->ReadLine();
        System::String^ result = RunTest(line);
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+result);
        System::Console::WriteLine ("Case #"+(i+1).ToString()+": "+result);
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
#define MIN(a,b) ((a)<(b)?(a):(b))
System::String^ RunTest (System::String^ t)
{
    System::String^ retval = "";
    {
        array<System::String^>^ split = t->Split();
        array<System::Int32>^ Vals = gcnew array<System::Int32>(split->Length);
        for (System::Int32 i=0; i<Vals->Length; i++)
        {
            Vals[i] = System::Convert::ToInt32(split[i]);
        }
        System::Int32 Sum = 0;
        System::Int32 MaxRate = 0;
        for (System::Int32 i=1; i<Vals->Length; i++)
        {
            if ((Vals[i-1] - Vals[i]) > 0)
            {
                Sum += Vals[i-1] - Vals[i];
            }
            if ((Vals[i-1] - Vals[i]) > MaxRate)
            {
                MaxRate = (Vals[i-1] - Vals[i]);
            }
        }
        retval += Sum.ToString() + " ";
        Sum = 0;
        for (System::Int32 i=0; i<Vals->Length-1; i++)
        {
            Sum += MIN(MaxRate, Vals[i]);
        }
        retval += Sum.ToString();
    }
    return retval;
}