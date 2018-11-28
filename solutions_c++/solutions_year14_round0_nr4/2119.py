//
//  main.cpp
//  Deceitful War
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
    void swap(int in1, int in2)
    {
        if(in1<0 || in1 >= size || in2 < 0 || in2 >= size)
            return;
        Type temp = *(data + in1);
        *(data + in1) = *(data + in2);
        *(data + in2) = temp;
    }
    
    ~Vector()
    {
        delete [] data;
    }
    
};

void LoadData(Vector<double> &naomi, Vector<double> &ken, ifstream & stream);

void ComputeResults(Vector<double> &naomi, Vector <double> &ken, int &war, int &dWar);
void WriteData(int dWar, int war,int in, ofstream & stream);
void BubbleSort(Vector<double> &data);

int main(int argc, const char * argv[])
{
    ifstream fin("D-small-attempt0.in.txt");
    ofstream fout("D-large1.out");
    int loop;
    fin>>loop;
    for(int i=1; i<=loop; i++) {
        Vector<double> naomi;
        Vector<double> ken;
        LoadData(naomi, ken,fin);
        BubbleSort(naomi);
        BubbleSort(ken);
        for(int i=0; i<naomi.getSize(); i++) {
            cout<<naomi.getAt(i)<<", ";
        }
        cout<<endl;
        for(int i=0; i<ken.getSize(); i++) {
            cout<<ken.getAt(i)<<", ";
        }
        cout<<endl;
        
        int war=0, dWar=0;
        ComputeResults(naomi, ken, war, dWar);
        WriteData(dWar,war, i, fout);
        
    }
    fin.close();
    fout.close();
    
    
    return 0;
}
void ComputeWar(Vector<double> naomi, Vector <double> ken, int &war) {
 
    
    int count = 0;
    while(naomi.getSize()) {
        if(naomi.getAt(0) > ken.getAt(0)) {
            naomi.deleteAt(0);
            ken.deleteAt(ken.getSize() -1);
            count ++;
        }
        else {
            naomi.deleteAt(0);
            ken.deleteAt(0);
        }
    }
    war = count;
    
}
void ComputeDWar(Vector<double> naomi, Vector <double> ken, int &dWar) {
    int count = 0;
    while(naomi.getSize()) {
        if(naomi.getAt(naomi.getSize() -1) < ken.getAt(ken.getSize() - 1)) {
            naomi.deleteAt(naomi.getSize() -1);
            ken.deleteAt(0);
        }
        else {
            naomi.deleteAt(naomi.getSize() -1);
            ken.deleteAt(ken.getSize() -1);
            count ++;
        }
    }
    dWar = count;
}

void ComputeResults(Vector<double> &naomi, Vector <double> &ken, int &war, int &dWar)
{
    
    
    ComputeWar(naomi, ken, war);
    ComputeDWar(naomi, ken, dWar);
}



void WriteData(int dWar,int war,int in, ofstream & stream)
{
    
    stream<<"Case #"<<in<<": "<<dWar<<" "<<war<<endl;
}


void LoadData(Vector<double> &naomi, Vector<double> &ken, ifstream & stream)
{
    int bloacksEachPerson;
    stream>>bloacksEachPerson;
    for(int i=0; i<bloacksEachPerson; i++) {
        double next;
        stream>>next;
        naomi.add(next);
    }
    for(int i=0; i<bloacksEachPerson; i++) {
        double next;
        stream>>next;
        ken.add(next);
    }
    
}
void BubbleSort(Vector<double> & data)
{
    for(int i=0; i<data.getSize()-1;i++)
    {
        for(int j=0;j<data.getSize()-1;j++)
        {
            if(data.getAt(j)<data.getAt(j+1))
            {
                data.swap(j, j+1);
            }
        }
    }
}
