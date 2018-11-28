#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

long long int a[2000];

struct palin {
    int a,b;
};

int find()
{
    long long int i,k,l,t,r,j,h,pt;
    int ct =0;
    for(i=1;i<=9;i++) {
        a[i] = i*i;
    }
    ct = 10;
    for(i=2;i<=6;i++) {
        if(i%2 == 0) {
              h = i/2;
              k = pow(10,h-1);
              l = pow(10,h);
              for(j=k;j<l;j++) {
                  t = j;
                  r = j;
                  while(t!=0) {
                      h = t%10;
                      r = r*10+h;
                      t = t/10;
                  }
                  a[ct] = r*r;
                  ct++;
              }
        } else {
            h = (i-1)/2;
            k = pow(10,h-1);
            l = pow(10,h);
            for(j=k;j<l;j++) {
                for(pt=0;pt<10;pt++) {
                     t = j;
                     r = j;
                     r = r*10+pt;
                  while(t!=0) {
                      h = t%10;
                      r = r*10+h;
                      t = t/10;
                  }
                  a[ct] = r*r;
                  ct++;
                }
            }
        }
    }
    return ct;
}

int check(long long int a[], long long int b[])
{
    int i,ct = 0,t,h,j;
    char s[20];
    for(i=1;i<1999;i++) {
        sprintf(s,"%lld",a[i]);
        t = strlen(s);
        if(t == 1) {
            b[ct] = a[i];
            ct++;
        } else if(t%2 == 0) {
            h = 1;
            for(j=0;j<t/2;j++) {
                if(s[j] != s[t-j-1]) {
                    h = 0;
                    break;
                }
            }
            if(h == 1) {
                b[ct] = a[i];
                ct++;
            }
        } else {
            h = 1;
            for(j=0;j<t/2;j++) {
                if(s[j] != s[t-j-1]) {
                    h = 0;
                    break;
                }
            }
            if(h == 1) {
                b[ct] = a[i];
                ct++;
            }
        }

    }
    return ct;
}

int main()
{
    int j,t,i,A,B,cnt,ct=0;
    cnt = find();
    long long int b[2000],r,h;
    cnt = check(a,b);
    scanf("%d",&t);
    for(i=0;i<t;i++) {
        ct = 0;
        scanf("%lld %lld",&r,&h);
        for(j=0;j<cnt;j++) {
            if(b[j]>=r && b[j]<=h)
            ct++;
        }
        printf("Case #%d: %d\n",i+1,ct);
    }
    return 0;
}
