// B_IHOP.cpp : main project file.

#include "stdafx.h"
#include <cstring>

using namespace System;

#define MAX_PANCAKES (10)

int NextMax (int* start, int current)
{
    while (current > 0 && start[current] == 0)
    {
        current--;
    }
    return current;
}

int Solve (int* freq, int max)
{
    int Best = max;
    if (max > 3)
    {
        // split len into i piles costing (i-1) moves
        int* ThisFreq = new int[max];
        for (int i=2; i<max; i++)
        {
            memcpy (ThisFreq, freq, sizeof(int)*(max));
            int This = (i-1) * freq[max];
            for (int j=0; j<i; j++)
            {
                ThisFreq[(max+j)/i] += freq[max];
            }
            This += Solve (ThisFreq, NextMax(ThisFreq, max-1));
            if (Best > This) Best = This;
        }
        delete[] ThisFreq;
    }
    return Best;
}

#define MIN(a,b) ((a)<(b)?(a):(b))
System::Int32 RunTest (System::String^ test)
{
    array<System::String^>^ split = test->Split();
    int PancakeFreq[MAX_PANCAKES] = {0};
    int MaxStack = 0;
    for (System::Int32 i=0; i<split->Length; i++)
    {
        System::Int32 num = System::Convert::ToInt32 (split[i]);
        if (MaxStack < num) MaxStack = num;
        PancakeFreq[num]++;
    }
    return Solve (PancakeFreq, MaxStack);
#if 0
    System::Int32 Best = MaxStack;
    System::Int32 Split = 0;
    do
    {
        // split the highest
        Split += PancakeFreq[MaxStack];
        PancakeFreq[MaxStack/2] += PancakeFreq[MaxStack];
        PancakeFreq[(MaxStack+1)/2] += PancakeFreq[MaxStack];
        PancakeFreq[MaxStack] = 0;
        while ((MaxStack > 0) && !PancakeFreq[MaxStack]) MaxStack--;
        if (Best > MaxStack + Split) Best = MaxStack + Split;
    } while (MaxStack > 0);
    return Best;
    int Minutes = 0;
    System::Boolean Done = false;
    while (!Done)
    {
        System::Int32 save = MaxStack/2;
        System::Int32 NumSplit = PancakeFreq[MaxStack];
        System::Int32 add = 0;
        for (System::Int32 i=MaxStack-NumSplit; i<MaxStack; i++)
        {
            add += PancakeFreq[i];
        }
        NumSplit += add;
        Done = !(save > NumSplit);
        if (!Done)
        {
            Minutes += NumSplit;
            while (NumSplit)
            {
                PancakeFreq[MaxStack/2] += PancakeFreq[MaxStack];
                PancakeFreq[(MaxStack+1)/2] += PancakeFreq[MaxStack];
                NumSplit -= PancakeFreq[MaxStack];
                PancakeFreq[MaxStack] = 0;
                MaxStack--;
            }
        }
        while (!PancakeFreq[MaxStack]) MaxStack--;
    }
    Minutes += MaxStack;
//#else
    int Worst = MaxStack;
    int* Current = PancakeFreq;
    while (Current < PancakeFreq+MaxStack)
    {
        // we could either split the max or let them eat
        System::Int32 max = PancakeFreq+MaxStack - Current;
        System::Int32 Freq = Current[max];
        System::Int32 Save = max/2;
        //System::Int32 next = NextMax(PancakeFreq, MaxStack-1);
        //Save = MIN (max-next, Save);
        //System::Int32 add = 0;
        //for (System::Int32 j=max-1; j>=max-Freq; j--)
        //{
        //    add += Current[j];
        //}
        if (Save > Freq)//+add)
        {
            // add freq minutes to split; Current does not move
            Minutes += Freq;
            Current[max/2]+=Freq;
            Current[(max+1)/2]+=Freq;
            Current[max] = 0;
            MaxStack = NextMax (PancakeFreq, MaxStack);
        }
        else
        {
            // once you stop splitting you do not split ever again
            // i think but for now, let's just brute force the count
            Minutes++;
            Current++;
        }
    }
    return MIN(Worst, Minutes);
    return Minutes;
#endif
}

int main(array<System::String ^> ^args)
{
    System::IO::TextReader^ rdr = gcnew System::IO::StreamReader(args[0]);
    System::String^ outname = args[0]->Substring(0,args[0]->LastIndexOf("."))+".out";
    System::IO::TextWriter^ wtr = gcnew System::IO::StreamWriter(outname);
    System::Int32 NumTests = System::Convert::ToInt32 (rdr->ReadLine());
    for (System::Int32 i=0; i<NumTests; i++)
    {
        rdr->ReadLine();
        wtr->WriteLine ("Case #"+(i+1).ToString()+": "+RunTest(rdr->ReadLine()).ToString());
    }
    rdr->Close();
    wtr->Close();
    return 0;
}
