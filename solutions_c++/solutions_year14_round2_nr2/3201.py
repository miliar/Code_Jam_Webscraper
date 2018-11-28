#include<stdio.h>
#include<iostream>
#include<math.h>
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

using namespace std;

unsigned int a,b,k,t,s,i,j,l,m,n,p,c,tt,f;

int ab[32], bb[32],kb[32],nb[32];

void binary(unsigned int num, int arr[]);

int main()
{
//freopen("a.txt", "rt", stdin);
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
scanf("%u",&t);
//t=1;
rep(i,t)
{
    scanf("%u %u %u",&a, &b, &k);
    printf("Case #%u: ",i+1);
    binary(k, kb);
    tt= 0;
    rep(j,a)
        rep(l,b)
        {
            f=0;
            binary(j, ab);
            binary(l, bb);
            //printf("Binary Eqivalent %u: ", j);    rep(p,32)        cout<<ab[p];            cout<<endl;
            //printf("Binary Eqivalent %u: ", l);    rep(p,32)        cout<<bb[p];            cout<<endl;
            s=0;
            rep(m,32)
                s += (ab[m] & bb[m]) * pow(2,31-m);

            if(s<k)
                tt++;
            /*for(n = 0; n < 32; n++)
                s += nb[n]*pow(2,31-n);
            printf("Binary Eqivalent of %u: ",s);    rep(p,32)        cout<<nb[p];
            cout<<endl;
            /*
            if(f)
                cout<<"no";
            else
                cout<<"yes";
            cout<<endl;*/
        }
        cout<<tt<<endl;
}
return 0;
}
//========================================================
void binary(unsigned int num, int arr[])
{
unsigned int mask=2147483648;   //mask = [1000 0000 0000 0000]

c=0;
while(mask > 0)
   {
   if((num & mask) == 0 )
         arr[c]=0;//printf("0");
   else
         arr[c]=1;//printf("1");
  mask = mask >> 1 ;
  c++;
   }
}
