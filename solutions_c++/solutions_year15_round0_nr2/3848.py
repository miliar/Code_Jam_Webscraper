//
//  main.cpp
//  codejam_infinite_house_of_pancakes
//
//  Created by Alexandru Andronache on 11/04/15.
//  Copyright (c) 2015 Alexandru Andronache. All rights reserved.
//

#include <iostream>
#include <vector>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");
FILE *h = fopen("bestsplit.txt", "r");

struct split
{
    split(int _x, int _y)
    {
        x = _x;
        y = _y;
    }
    int x;
    int y;
};

using namespace std;

int T, D;
vector<int> heap;
vector<int> initial;
vector<split> bestSplit;

int getParent(int p)
{
    if (p % 2 == 0) return (p / 2) - 1;
    else return p / 2;
}

void switchVar(int& x, int& y)
{
    int t = x;
    x = y;
    y = t;
}

void addToHeap(int x)
{
    heap.push_back(x);
    int pos = heap.size() - 1;
    while (pos != 0 && heap[getParent(pos)] < heap[pos])
    {
        switchVar(heap[getParent(pos)], heap[pos]);
        pos = getParent(pos);
    }
}

int removeHeadFromHeap()
{
    int tmp = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    
    int pos = 0;
    while ((2 * pos + 1 < heap.size() && heap[pos] < heap[2 * pos + 1]) ||
           (2 * pos + 2 < heap.size() && heap[pos] < heap[2 * pos + 2]))
    {
        
        if (heap[2 * pos + 1] > heap[2 * pos + 2])
        {
            switchVar(heap[pos], heap[2 * pos + 1]);
            pos = 2 * pos + 1;
        }
        else
        {
            switchVar(heap[pos], heap[2 * pos + 2]);
            pos = 2 * pos + 2;
        }
    }
    
    return tmp;
}

int main(int argc, const char * argv[])
{
    bestSplit.push_back(split(0, 0));
    for (int i = 1; i < 1100; ++i)
    {
        int x, y;
        fscanf(h, "%d %d", &x, &y);
        bestSplit.push_back(split(x, y));
    }
    
    fscanf(f, "%d", &T);
    
    for (int t = 1; t <= T; ++t)
    {
        fscanf(f, "%d", &D);
        heap.clear();
        initial.clear();
        for (int i = 0; i < D; ++i)
        {
            int x;
            fscanf(f, "%d", &x);
            addToHeap(x);
            initial.push_back(x);
        }
        
        int minim = heap[0], counter = 0;
        while (heap[0] != 1)
        {
            counter++;
            int t = removeHeadFromHeap();
            addToHeap(bestSplit[t].x);
            addToHeap(bestSplit[t].y);
//            if (t % 2 == 0)
//            {
//                addToHeap(t / 2);
//                addToHeap(t / 2);
//            }
//            else
//            {
//                addToHeap(t / 2 + 1);
//                addToHeap(t / 2);
//            }
            if (minim > heap[0] + counter)
            {
                minim = heap[0] + counter;
            }
        }
        
        heap.clear();
        for (int i = 0; i < D; ++i)
        {
            addToHeap(initial[i]);
        }
        
        counter = 0;
        while (heap[0] != 1)
        {
            counter++;
            int t = removeHeadFromHeap();
            if (t % 2 == 0)
            {
                addToHeap(t / 2);
                addToHeap(t / 2);
            }
            else
            {
                addToHeap(t / 2 + 1);
                addToHeap(t / 2);
            }
            if (minim > heap[0] + counter)
            {
                minim = heap[0] + counter;
            }
        }
//        for (auto it : initial)
//            fprintf(g, "%d ", it);
        fprintf(g, "Case #%d: %d\n", t, minim);
    }
    
    return 0;
}

