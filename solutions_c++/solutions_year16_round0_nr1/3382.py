// A_Counting_Sheep.cpp : main project file.

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
        if (result)
        {
            wtr->WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
            System::Console::WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
        }
        else
        {
            wtr->WriteLine ("Case #"+(i+1).ToString()+": "+"INSOMNIA");
            System::Console::WriteLine ("Case #"+(i+1).ToString()+": "+"INSOMNIA");
        }
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
System::Int16 GetDigits (System::Int64 x);
System::Int32 RunTest (System::String^ str)
{
    System::Int16 Found = 0x0000;
    System::Int32 test = System::Convert::ToInt32 (str);
    System::Int32 shift = 1;
    while ((test > 0) && (test%10) == 0)
    {
        Found |= 1;
        test /= 10;
        shift *= 10;
    }
    System::Int32 i;
    for (i=1; i<1000000; i++)
    {
        System::Int16 mask = GetDigits ((System::Int64) test * (System::Int64) i);
        Found |= mask;
        if (Found == 0x3FF) break;
    }
    return (Found == 0x3FF)?(i*test*shift):0;
}

System::Int16 GetDigits (System::Int64 x)
{
    System::Int16 retval = 0;
    System::Int32 rem;
    while (x)
    {
        rem = x%10;
        retval |= (1<<rem);
        x/=10;
    }
    return retval;
}
