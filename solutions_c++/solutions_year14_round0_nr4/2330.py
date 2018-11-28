//
//  main.cpp
//  prac
//
//  Created by Deshmukh  on 17/03/14.
//  Copyright (c) 2014 Deshmukh . All rights reserved.
//

#include <iostream>
#include<string>
#include<ctime>
#include<fstream>
#include<limits>


int Partition(double a[], int beg, int end);
void QuickSort(double a[], int beg, int end);


int main(int argc, const char * argv[])
{   using namespace std;
    ofstream output;
    ifstream input;
    int t,t1=1,n,i,j,nd,nf,ns,ne,ks,ke,flag;
    input.open("/Users/deshmukh/Desktop/c/Udit/codejam/input/sample");
    output.open("/Users/deshmukh/Desktop/c/Udit/codejam/output/output1.txt");
    input>>t;
    while(t1<=t){
        
        input>>n;
        input.precision(5);
        double naomi[1000],ken[1000];
        for(i=0;i<n;i++)
            input>>naomi[i];
        for(i=0;i<n;i++)
            input>>ken[i];
        nd=n;
        nf=n;
        QuickSort(naomi,0,n-1);
        QuickSort(ken, 0, n-1);
        ns=0;ne=n-1;
        ks=0;ke=n-1;
        while(1){
            flag=0;
            for(i=ns,j=ks;i<=ne && j<=ke;i++,j++){
                if(ken[j]>naomi[i]){
                    ke--;
                    ns++;
                    nd--;
                    flag=1;
                    break;
                }
            }
            if(flag==0)
                break;
        }
        int k[1000]{};
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(ken[j]>naomi[i] && k[j]==0){
                    nf--;
                    k[j]=1;
                    break;
                }
            }
        }
        
        output<<"Case #"<<t1<<": "<<nd<<" "<<nf<<"\n";
        
        t1++;
        
    }
    
    
    
    
    
   
    return 0;
}




int Partition(double a[], int beg, int end)          //Function to Find Pivot Point
{
    int p=beg,loc;
    double pivot=a[beg];
    
    for(loc=beg+1;loc<=end;loc++)
    {
        if(pivot>a[loc])
        {
            a[p]=a[loc];
            a[loc]=a[p+1];
            a[p+1]=pivot;
            
            p=p+1;
        }
    }
    return p;
}


void QuickSort(double a[], int beg, int end)
{
    if(beg<end)
    {
        int p=Partition(a,beg,end);                       //Calling Procedure to Find Pivot
        
        QuickSort(a,beg,p-1);                             //Calls Itself (Recursion)
        QuickSort(a,p+1,end);			              //Calls Itself (Recursion)
    }
}