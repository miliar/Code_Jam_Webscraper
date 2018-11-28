#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include "Pancakes.h"

using namespace std;

vector<bool> faces;
int frame;
int flips;

Pancakes::Pancakes()
{
}

string Pancakes::countFlips(string pile)
{
    setFaces(pile);

    while(frame > 0)
    {
        flipTopPositives();
        flipStack(frame);
    }

    return intToString(flips);
}

void Pancakes::flipTopPositives()
{
    for(int i = 0; i < frame; i++)
    {
        if(!faces[i])
        {
            flipStack(i);
        }
    }
    setFramePointer();
}

void Pancakes::flipStack(int stackPointer)
{
    if(stackPointer == 0)
    {
        return;
    }

    vector<bool> flipStack(frame);
    for(int i = 0; i < frame; i++)
    {
        flipStack[i] = !faces[frame-i-1];
    }
    for(int i = 0; i < frame; i++)
    {
        faces[i] = flipStack[frame-i-1];
    }
    setFramePointer();
    flips++;
}

void Pancakes::setFramePointer()
{
    for(int i = frame-1; i >= 0 ; i--)
    {
        if(!faces[i])
        {
            frame = i + 1;
            return;
        }
    }
    frame = 0;
}

void Pancakes::setFaces(string pile)
{
    flips = 0;
    int stackSize = pile.length();
    faces.resize(0);
    char pancake;
    for(int i = 0; i < stackSize; i++)
    {
        pancake = pile.at(i);
        switch(pancake)
        {
            case '+': faces.push_back(true); break;
            case '-': faces.push_back(false); break;
        }
    }
    frame = faces.size();
    setFramePointer();
}

string Pancakes::intToString(int number)
{
    stringstream ss;
	ss << number;
	return ss.str();
}
