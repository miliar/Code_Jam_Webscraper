#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <fstream>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#define REP(i,n) for(int i=0;i<(n);++i)
#define ZERO(x) memset(x,0,sizeof(x))

using namespace std;
int a[100][100];
int max1[100];
int max2[100];
//2 9
//55 29 42 15 43 41 80 29 1

//6 14 19 31 32 36 49 94
int func(std::vector<int> myvector, int A, int N){
    int i=0;int count=0;int minIfwedrop=INT_MAX;
    for(std::vector<int>::iterator it=myvector.begin(); it!=myvector.end(); ++it, i++){
        //cout<< *it<<" ";
        if(*it<A)
        {A=A+*it;continue;}
        //else
        if(A==1) // case for 1
            return N-i;
        int no=0;
        for(;A<=*it; no++, A=A+A-1);
        if(no < N-i)
        {       
            A=A+(*it); 
            
            minIfwedrop= (N-i)+count < minIfwedrop?(N-i+count):minIfwedrop;  
            count+= no;   
        } 
        else
            return (N-i)+count < minIfwedrop?N-i+count:minIfwedrop;
        
    }
    return count;
    //cout <<endl;
    
}

int main(){
    int T;int N; int A;
    scanf("%d",&T);
    ofstream myfile;
    
    myfile.open ("/home/ds/codes/output2.txt");
    for(int ii=1; ii<=T;ii++){
        scanf("%d",&A);scanf("%d",&N);
        int * p; p= (int*)malloc(N*sizeof(int));
        for(int j=0; j<N;j++)
            scanf("%d",&p[j]);
        std::vector<int> myvector (p, p+N);
        std::sort (myvector.begin(), myvector.end()); 
        
        myfile << "Case #"<<ii<<": "<<func(myvector, A,N)<<endl;

    }
    myfile.close();
    return 0;
}
 
