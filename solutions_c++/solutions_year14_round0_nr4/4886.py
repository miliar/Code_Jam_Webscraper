#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stack>
#define Maxn 200
using namespace std;

struct tri
{
    int x,y,dt;
} A[Maxn*Maxn],B[Maxn];


int a,b;

int cmp(tri A,tri B)
{
    if (A.x==B.x) return A.y<B.y;
    return A.x<B.x;
}

int cmp1(tri A,tri B)
{
    if ( A.x==B.x ){
        if (A.y<B.y) return -1;
        if (A.y==B.y) return 0;
        return 1;
    }
    if (A.x<B.x) return -1;
    return 1;
}



int main()
{
    // freopen("1.in","r",stdin);
    char s1[80];
    puts("Input number of trible A");
    cin>>a;
    puts("Input trible A");
    for (int  i=1;i<=a;i++)
        cin>>A[i].x>>A[i].y>>A[i].dt;
    puts("Input number of trible B");
    cin>>b;
    puts("Input trible B");
    for (int  i=1;i<=b;i++)
        cin>>B[i].x>>B[i].y>>B[i].dt;
    sort(A+1,A+a+1,cmp);
    sort(B+1,B+b+1,cmp);

    int p1=a,p2=b,p3= a+b+1;

    while(p1&&p2)
    {
        // cout<<p1<<" "<<p2<<" "<<p3<<endl;
        if (cmp1(A[p1],B[p2])==0)
        {
            A[--p3]=A[p1--];
            A[p3].dt+=B[p2--].dt;
        }
        else if (cmp1(A[p1],B[p2])==1)
            A[--p3]=A[p1--];
        else 
            A[--p3]=B[p2--];
    }
    while (p1) A[--p3]=A[p1--];
    while (p2) A[--p3]=B[p2--];
    
    // for (int i=p3;i<=a+b;i++) cout<<A[i].x<<" "<<A[i].y<<" "<<A[i].dt<<endl;
    
    for (int i=p3;i<=a+b;i++)
        A[i-p3+1]=A[i];
    puts("The answer is :");
    int num=a+b-p3+1;
    for (int i=1;i<=num;i++) 
        cout<<A[i].x<<" "<<A[i].y<<" "<<A[i].dt<<endl;
    
    return 0;
}