#include<iostream>
#include<queue>
#include<stdio.h>

using namespace std;

int main() {
    FILE* fin=fopen("B-small-attempt2.in","r");
    FILE* fout=fopen("out.txt","w");
    int t;
    priority_queue<pair<int,int>> pq;
    fscanf(fin,"%d",&t);
    for(int tt=1;tt<=t;tt++){
        int n,b,m[1010];
        int mul=1,sum=0;
        pq = priority_queue<pair<int,int>>();
        fscanf(fin,"%d %d",&b,&n);
        for(int i=1;i<=b;i++) {
            fscanf(fin,"%d",&m[i]);
            pq.push(make_pair(0,-i));
            mul*=m[i];
        }
        for(int i=1;i<=b;i++)
            sum+=mul/m[i];
        n%=sum;
        if(n==0)
            n=sum;
        int now=1;
        while(now<n) {
            pair<int,int> x = pq.top();
            pq.pop();
            pq.push(make_pair(x.first-m[-x.second],x.second));
            now++;
        }
        fprintf(fout,"Case #%d: %d\n",tt,-pq.top().second);
    }
    fclose(fin);
    fclose(fout);
}
