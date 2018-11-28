//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <time.h>
#include <sstream>
//    clock_t lim = clock() + 1.9*CLOCKS_PER_SEC;
//        if (clock() >= lim)break;
//#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define ULL unsigned long long
const int MAXN = 1010;
const int mod = 1e9+7;
const int INF = 0x3f3f3f3f;
const double pi = acos(-1.0);
const double eps = 1e-6;
/* ***********************************************************
//����ͼƥ�䣨�������㷨��DFSʵ�֣� (�ڽӾ�����ʽ)
//��ʼ���� g[][]���߶���Ļ������
//����g[i][j]��ʾi->j������߾Ϳ����ˣ���������ұߵ�ƥ��
//gû�б��������ʼ��Ϊ0
//uN��ƥ����ߵĶ������� vN��ƥ���ұߵĶ�����
//���ã� res=hungary();������ƥ����
//�ŵ㣺�����ڳ���ͼ�� DFS������·��ʵ�ּ���������
//ʱ�临�Ӷ�:O(VE)
//*************************************************************/
//�����Ŵ�0��ʼ��
map<string,int>mp1,mp2;
string s1,s2;
int uN,vN;//u,v����Ŀ��ʹ��ǰ����븳ֵ
int g[MAXN][MAXN];//�ڽӾ���
int linker[MAXN];
bool used[MAXN];
bool dfs(int u)
{
    for(int v = 1; v <= vN; v++)
        if(g[u][v] && !used[v])
        {
            used[v] = true;
            if(linker[v] == -1 || dfs(linker[v]))
            {
                linker[v] = u;
                return true;
            }
        }
    return false;
}
int hungary()
{
    int res = 0;
    memset(linker,-1,sizeof(linker));
    for(int u = 1; u <= uN; u++)
    {
        memset(used,false,sizeof(used));
        if(dfs(u))res++;
    }
    return res;
}
int main()
{
//    freopen("in.in","r",stdin);
//    freopen("out.out","w",stdout);
    int t,n,cas=1;
    cin>>t;
    while(t--){
        cin>>n;
        int cnt=0;
        uN=1;
        vN=1;
        mp1.clear();
        mp2.clear();
        memset(g,0,sizeof g);
        for(int i=0;i<n;i++){
            cin>>s1>>s2;
            if(!mp1[s1])
                mp1[s1]=uN++;
            if(!mp2[s2])
                mp2[s2]=vN++;
            g[mp1[s1]][mp2[s2]]=1;
        }
        int mm=hungary();
        printf("Case #%d: ",cas++);
        cout<<n-(uN+vN-2-mm)<<endl;
    }
    return 0;
}
//string s1,s2;
//bool same(string s,int x)
//{
//    string ss;
//    int m=s.size();
//    stringstream tmp;
//    tmp.width(s.size());
//    tmp.fill('0');
//    tmp<<x;
//    tmp>>ss;
////    while(m--){
////        ss.append(string(x%10));
////        x/=10;
////    }
////    reverse(ss.begin(),ss.end());
//    for(int i=0; i<s.size(); i++)
//    {
//        if(s[i]=='?')
//            continue;
//        else if(s[i]!=ss[i])
//            return 0;
//    }
//    return 1;
//}
//int main()
//{
//    freopen("in.in","r",stdin);
//    freopen("out.out","w",stdout);
//    int t,n,cas=1;
//    cin>>t;
//    while(t--)
//    {
//        cin>>s1>>s2;
//        int l=s1.size();
//        int ans1,ans2,dis=9999;
//        if(l==1)
//        {
//            for(int i=0; i<=9; i++)
//            {
//                for(int j=0; j<=9; j++)
//                {
//                    if(same(s1,i)&&same(s2,j)&&abs(i-j)<dis)
//                    {
//                        ans1=i;
//                        ans2=j;
//                        dis=abs(i-j);
//                    }
//                }
//            }
//        }
//        else if(l==2)
//        {
//            for(int i=0; i<=99; i++)
//            {
//                for(int j=0; j<=99; j++)
//                {
//                    if(same(s1,i)&&same(s2,j)&&abs(i-j)<dis)
//                    {
//                        ans1=i;
//                        ans2=j;
//                        dis=abs(i-j);
//                    }
//                }
//            }
//        }
//        else if(l==3)
//        {
//            for(int i=0; i<=999; i++)
//            {
//                for(int j=0; j<=999; j++)
//                {
//                    if(same(s1,i)&&same(s2,j)&&abs(i-j)<dis)
//                    {
//                        ans1=i;
//                        ans2=j;
//                        dis=abs(i-j);
//                    }
//                }
//            }
//        }
//        printf("Case #%d: ",cas++);
//        cout.width(s1.size());
//        cout.fill('0');
//        cout<<ans1<<" ";
//        cout.width(s1.size());
//        cout.fill('0');
//        cout<<ans2<<endl;
//    }
//    return 0;
//}
