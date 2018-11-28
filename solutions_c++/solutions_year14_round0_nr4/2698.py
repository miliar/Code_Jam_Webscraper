#include <cstdio>
#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <functional>
using namespace std;
int n;
vector<long double> pn,pk;
int playde()
{
    int kquick,kslow,tquick,tslow,total=0;
      kquick=tquick=0;
      kslow=tslow=n-1;
      for(int i=0;i<n;i++)//i is tianji the most quick
      {
         //�����������ȹ����������ʱ �����������������������
         if(pn[tquick]>pk[kquick])
         {
             total++;
             kquick++;
             tquick++;
         }
         //�����������ȹ�����������ʱ �������������������������
         else if(pn[tquick]<pk[kquick])
         {
              tslow--;
              kquick++;
         }
         else//j is tianji
         {
             for(int j=tslow,h=kslow;j>=tquick;j--,h--)
             {
                 if(pn[j]>pk[h])//�������������ȹ������������ʱ ���������������������������
                 {
                     total++;
                     tslow--;
                     kslow--;
                 }
                 else // �������������������������
                 {
                     if(pn[j]<pk[i])
                     {
                         tslow--;
                         kquick++;
                     }
                     tslow=--j;
                     kslow=h;
                     break;
                 }
             }
         }
         if(tquick>tslow)
           break;
      }
     return  total;
}
int playn()
{
    int i=0,j=0;
    while (j<n)
    {
        while (pn[i]>pk[j] && j>=0) ++j;
        if (j>=n) break;
        ++i;
        ++j;
    }
    return n-i;
}
int main()
{
    freopen("out.txt","r",stdin);
    freopen("oo.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--)
    {
        pn.clear();
        pk.clear();
        cin>>n;
        for (int i=0;i<n;++i)
        {
            long double t;
            cin>>t;
            pn.push_back(t);
        }
        for (int i=0;i<n;++i)
        {
            long double t;
            cin>>t;
            pk.push_back(t);
        }
        sort(pn.begin(),pn.end());
        sort(pk.begin(),pk.end());
        int aa=playn();
        sort(pn.begin(),pn.end(),greater<long double >());
        sort(pk.begin(),pk.end(),greater<long double >());

       printf("Case #%d: %d %d\n",++cas,playde(),aa);
    }
}
