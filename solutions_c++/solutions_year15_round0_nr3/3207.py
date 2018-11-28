#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define _1_  1
#define _n1_ 2
#define _i_  3
#define _ni_ 4
#define _j_  5
#define _nj_ 6
#define _k_  7
#define _nk_ 8

int comp(int oldv, char newv )
{
    if(oldv==0)
    {
        switch(newv)
        {
            case 'i': return _i_;
            case 'j': return _j_;
            case 'k': return _k_;
        }
    }
    switch(oldv)
    {
        case _1_:
                 switch(newv)
                 {
                    case 'i': return _i_;
                    case 'j': return _j_;
                    case 'k': return _k_;
                 }
                 break;
       case _n1_:
                 switch(newv)
                 {
                    case 'i': return _ni_;
                    case 'j': return _nj_;
                    case 'k': return _nk_;
                 }
                 break;

        case _i_:
                switch(newv)
                 {
                    case 'i': return _n1_;
                    case 'j': return _k_;
                    case 'k': return _nj_;
                 }
                 break;
        case _ni_:
                switch(newv)
                 {
                    case 'i': return _1_;
                    case 'j': return _nk_;
                    case 'k': return _j_;
                 }
                 break;
        case _j_:
                switch(newv)
                 {
                    case 'i': return _nk_;
                    case 'j': return _n1_;
                    case 'k': return _i_;
                 }
                 break;
        case _nj_:
                switch(newv)
                 {
                    case 'i': return _k_;
                    case 'j': return _1_;
                    case 'k': return _ni_;
                 }
                 break;
        case _k_:
                switch(newv)
                 {
                    case 'i': return _j_;
                    case 'j': return _ni_;
                    case 'k': return _n1_;
                 }
                 break;
        case _nk_:
                switch(newv)
                 {
                    case 'i': return _nj_;
                    case 'j': return _i_;
                    case 'k': return _1_;
                 }
                 break;

    }
    printf("error\n");

}

int main() {
  int T;
  int cases;
  int D1;
  int D2;
  char chars[10001];
  int acum;
  int ii,jj;

  freopen ("C-small-attempt0.in","r",stdin);
  freopen ("my.txt","w",stdout);

  scanf ("%d", &T);

  for(int cases=1;cases<=T;cases++)
  {
    acum=0;
    ii=0;jj=0;
    printf("Case #%d: ",cases);
    scanf("%d",&D1); //printf("D1 %d\n",D1);
    scanf("%d",&D2); //printf("D2 %d\n",D2);
    scanf("%s", chars);
    for(int i=0;i<D2;i++)
    {
        //printf("i %d\n",i);
        for(int j=0;j<D1;j++)
        {
             //scanf("%c",&ch);
            //printf("j %d\n",j);
            //printf("%c",chars[j]);

            acum = comp(acum, chars[j] );
            //printf("acum %d\n",acum);
            if(ii==0 && (acum==_i_ || acum==_ni_))
            {
              ii=1;
              if(acum==_ni_)
                acum=_n1_;
              else
                acum=_1_;


            }
            else if(ii==1 && jj==0 && (acum==_j_ || acum==_nj_))
            {
                jj=1;
                if(acum==_nj_)
                  acum=_n1_;
                else
                    acum=_1_;
            }

        }
        //printf("\n");
    }
    //printf("acum==%d && %d && %d\n",acum , jj , ii);
    if(acum==_k_ && jj && ii)
        printf("YES\n");
    else
        printf("NO\n");

 }
  //  printf("%d\n",comp(0, 'j' ));

  fclose (stdout);
  fclose (stdin);

  return 0;
}
