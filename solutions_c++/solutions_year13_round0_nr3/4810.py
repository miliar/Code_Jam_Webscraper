#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;
int palindrome (int n) // function for find "is n a palindrome number"?
{
    char c[7];
    //char c=itoa(n,c,n);
    sprintf(c,"%d",n); // transform n(integer) into string 'c'
    int a = atoi(strrev(c)); // transform inverse of 'c' into integer number
    if (a == n) return 1; // check if n is equal to inverse of n
    else return 0;
}
int sqr(int n){
    double r=sqrt(n);
    int c=r/1;
    if(r-c==0) return 1;
    else return 0;
}
main(){

   freopen("C-small-attempt1.in","r",stdin);
   freopen("C-small-attempt1.out","w",stdout);
    int test,N;
    cin>>N;
    for(test=0;test<N;test++)
    {
        int a,b;
        cin>>a>>b;
        int i,c=0;
        for(i=a;i<=b;i++){
        if(palindrome(i)&&i!=676)
            if(sqr(i))
                c++;}
        cout<<"Case #"<<test+1<<": "<<c<<endl;

    }
}
