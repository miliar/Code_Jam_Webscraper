//
//  main.cpp
//  GCJ quaternions
//
//  Created by Rafał Stempowski on 11.04.2015.
//  Copyright (c) 2015 Rafał Stempowski. All rights reserved.
//

#include <iostream>


char tab[4][4];





struct quat{
    bool pos;
    char a;
    quat(char c,bool posi)
    {
        a=c;
        pos=posi;
    }
    quat()
    {
        a=0;
        pos=1;
    }
    quat operator=(quat b)
    {
        a=b.a;
        pos=b.pos;
        return *this;
    }
    bool operator==(quat b)
    {
        if(a==b.a && pos==b.pos)
            return true;
        else
            return false;
    }
    quat operator*(quat b)
    {
        bool ret=(pos ? b.pos : !b.pos );
        if(a=='1')
        {
            return quat(b.a,ret);
        }
        else if(a=='i')
        {
           switch(b.a)
            {
                case '1':
                    return quat('i',ret);
                case 'i':
                    return quat('1',!ret);
                case 'j':
                    return quat('k',ret);
                case 'k':
                    return quat('j',!ret);
            }
        }
        else if(a=='j')
        {
            switch(b.a)
            {
                case '1':
                    return quat('j',ret);
                case 'i':
                    return quat('k',!ret);
                case 'j':
                    return quat('1',!ret);
                case 'k':
                    return quat('i',ret);
            }
        }
        else if(a=='k')
        {
            switch(b.a)
            {
                case '1':
                    return quat('k',ret);
                case 'i':
                    return quat('j',ret);
                case 'j':
                    return quat('i',!ret);
                case 'k':
                    return quat('1',!ret);
            }
        }
        
        return quat('1',ret);
    }
    
};


class zad
{
    quat* tab1;
    quat* tab2;
    quat* tab3;
    bool is_beg;
    int ile;
    int ile_wesz;
    int ile_tab2;
public:
    zad(int a,int b)
    {
        is_beg=false;
        ile=a*b;
        ile_wesz=0;
        ile_tab2=0;
        tab1=new quat('1',1);
        tab2=nullptr;
        tab3=nullptr;
        
    }
    void Dodaj(quat tmp)
    {
        if(!is_beg)
        {
            *tab1=*tab1*tmp;
            if(*tab1==quat('i',1))
                is_beg=true;
            ile_wesz++;
        }
        else
        {
            if(!tab2)
                tab2=new quat[ile-ile_wesz];
            tab2[ile_tab2]=tmp;
            ile_tab2++;
        }
    
    }
    bool Rob()
    {
        //if(ile_wesz==ile)
          //  return false;
        tab3=new quat;
        if(ile_tab2<2)
            return false;
        *tab3=tab2[ile_tab2-1];
        ile_tab2--;
        while(!(*tab3==quat('k',1)))
        {
            *tab3=tab2[ile_tab2-1]*(*tab3);
            ile_tab2--;
            if(ile_tab2==0)
                return false;
        }
        quat wynik('1',1);
        
        while(ile_tab2!=0)
        {
            wynik=tab2[ile_tab2-1]*wynik;
            ile_tab2--;
        }
        
        return (wynik==quat('j',1) ? true : false);
    }
    
};





int main(int argc, const char * argv[])
{
    FILE *pFile;
    pFile= fopen("/Users/rafal/Downloads/A-large.in","r");
    
    int t,l,x;
    char tmp;
    quat* tap;
    fscanf(pFile,"%d\n",&t);
    for(int h=0;h<t;h++)
    {
        
        fscanf(pFile,"%d %d\n",&l,&x);
        tap=new quat[l];
        zad wyn(l,x);
        for(int g=0;g<l;g++)
        {
            fscanf(pFile,"%c",&tmp);
            tap[g]=quat(tmp,1);
            wyn.Dodaj(tap[g]);
        }
        for(int g=0;g<x-1;g++)
        {
            for(int f=0;f<l;f++)
                wyn.Dodaj(tap[f]);
        }
        
        printf("\nCase #%d: ",h+1);
        (wyn.Rob() ? printf("YES") : printf("NO"));
        
        
        
        
    }
    
    
    
    
    return 0;
}
