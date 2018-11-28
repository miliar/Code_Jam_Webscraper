// B_Haircut.cpp : main project file.

#include "stdafx.h"

using namespace System;
System::Int32 RunTest (System::String^ s1, System::String^ s2);

int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        System::String^ line1 = rdr->ReadLine();
        System::String^ line2 = rdr->ReadLine();
        System::Int32 result = RunTest(line1, line2)+1;
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
        System::Console::WriteLine ("Case #"+(i+1).ToString()+": "+result.ToString());
    }
    rdr->Close();
    wtr->Close();
    return 0;
}

System::Int32 MinIdx (array<System::Int32>^ times)
{
    System::Int32 retval = -1;
    System::Int32 MinTime = System::Int32::MaxValue;
    for (System::Int32 i=0; i<times->Length; i++)
    {
        if (times[i] < MinTime)
        {
            MinTime = times[i];
            retval = i;
            if (MinTime == 0) break;
        }
    }
    return retval;
}

#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
System::Int64 GCD (System::Int64 a, System::Int64 b)
{
    System::Int64 min = MIN(a,b);
    System::Int64 max = MAX(a,b);
    System::Int64 rem;
    while ((rem = (max % min)) != 0)
    {
        max = min;
        min = rem;
    }
    return min;
}

System::Int64 LCM (System::Int64 a, System::Int64 b)
{
    System::Int64 gcd = GCD(a,b);
    return a/gcd*b;
}

System::Int32 RunTest (System::String^ s1, System::String^ s2)
{
    System::Int32 retval = 0;
    array<System::String^>^ split1 = s1->Split();
    array<System::String^>^ split2 = s2->Split();
    System::Int32 Me = System::Convert::ToInt32(split1[1]);
    array<System::Int32>^ Barbers = gcnew array<System::Int32>(split2->Length);
    System::Int64 LeastMult = 1;
    System::Int32 MinBarber;
    System::Int32 MinTime = System::Int32::MaxValue;
    for (System::Int32 i=0; i<Barbers->Length; i++)
    {
        Barbers[i] = System::Convert::ToInt32(split2[i]);
        LeastMult = LCM(LeastMult, Barbers[i]);
        if (Barbers[i] <= MinTime)
        {
            MinTime = Barbers[i];
            MinBarber = i;
        }
    }
    System::Int32 CompleteSet = 0;
    for (System::Int32 i=0; i<Barbers->Length; i++)
    {
        CompleteSet += System::Int32(LeastMult/(System::Int64)Barbers[i]);
    }
    Me %= CompleteSet;
    array<System::Int32>^ Times = gcnew array<System::Int32>(split2->Length);
    Times->Initialize();
    if (Me == 0)
    {
        retval = MinBarber;
    }
    else
    {
        for (System::Int32 i=0; i<Me; i++)
        {
            retval = MinIdx (Times);
            if (Times[retval] > 0)
            {
                System::Int32 MinTime = Times[retval];
                for (System::Int32 j=0; j<Times->Length; j++)
                {
                    Times[j] -= MinTime;
                }
            }
            Times[retval] = Barbers[retval];
        }
    }
    return retval;
}