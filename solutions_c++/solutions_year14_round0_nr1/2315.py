//
//  main.cpp
//  Magic Trick
//
//  Created by Umair Akhtar on 12/04/2014.
//  Copyright (c) 2014 Umair Ahmad. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

template <typename Type>
class Vector {
    Type *data;
    int size, maxSize;
    void doubleSize()
    {
        Type *nData = new Type[maxSize*2];
        for(int i=0; i<size; i++)
            *(nData + i) = *(data + i);
        delete [] data;
        maxSize = maxSize * 2;
        data = nData;
    }
public:
    Vector<Type>()
    {
        maxSize = 2;
        data = new Type [maxSize];
        size =0;
    }
    Vector<Type>(Vector<Type> &v) {
        maxSize = v.maxSize;
        data = new Type[maxSize];
        size = 0;
        for(int i=0; i< v.size; i++)
        {
            this->add(v.getAt(i));
        }
    }
    
    Vector<Type> operator = (Vector<Type> &v)
    {
        if(this==&v)
            return *this;
        int s = size;
        for(int i = v.getSize(); i<s; i++)
            this->deleteAt(0);
        
        for(int i=0; i< v.getSize(); i++)
        {
            try {
                
                this->setAt(i, v.getAt(i));
            } catch (int a) {
                this->add(v.getAt(i));
            }
        }
        
        return *this;
    }
    
    Type getAt(int index)
    {
        if(index<size)
            return *(data + index);
        throw (std::string) "Array out of bounds";
    }
    void setAt(int index, Type n)
    {
        if(index >= size) throw 0;
        data[index] = n;
    }
    void add(Type d)
    {
        if(size == maxSize)
            doubleSize();
        *(data + size) = d;
        size++;
    }
    void deleteAt(int index) {
        if(index >= 0 && index <size) {
            for(int i=index; i<size-1; i++) {
                *(data + i) = *(data + i + 1);
            }
            size --;
        }
    }
    int getSize()
    {
        return size;
    }
    
    ~Vector()
    {
        delete [] data;
    }
    
};

void LoadData(int firstData[][4], int secondData[][4],int & firstRow,int & secondRow, ifstream & stream);
Vector<int> * intersect(int firstData[], int secondData[]);
void WriteData(Vector<int> * data,int in, ofstream & stream);


int main(int argc, const char * argv[])
{
    ifstream fin("A-small-attempt0.in.txt");
    ofstream fout("A-small1.out");
    int loop;
    fin>>loop;
    for(int i=1; i<=loop; i++) {
        
        int firstData[4][4], secondData[4][4];
        int firstRow, secondRow;
        LoadData(firstData, secondData,firstRow , secondRow,fin);
        Vector<int>* intersected = intersect(firstData[firstRow-1], secondData[secondRow-1]);
        WriteData(intersected, i, fout);
        
    }
    fin.close();
    fout.close();
    
    
    return 0;
}

Vector<int> * intersect(int firstData[], int secondData[]) {
    Vector<int> * toR = new Vector<int >;
    for(int i=0; i<4 ; i++) {
        for(int j=0; j<4; j++) {
            if(firstData[i] == secondData[j])
                toR->add(firstData[i]);
        }
    }
    return toR;
    
}

void WriteData(Vector<int> * data,int in, ofstream & stream)
{
    if(data->getSize() == 0) stream<<"Case #"<<in<<": "<<"Volunteer cheated!"<<endl;
    else if(data->getSize() == 1) stream<<"Case #"<<in<<": "<<data->getAt(0)<<endl;
    else if(data->getSize() > 1) stream<<"Case #"<<in<<": "<<"Bad magician!"<<endl;
    
}

void LoadData(int firstData[][4], int secondData[][4],int & firstRow,int & secondRow, ifstream & stream)
{
    stream>>firstRow;
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            stream>>firstData[i][j];
        }
    }
    
    stream>>secondRow;
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            stream>>secondData[i][j];
        }
    }
    
}
