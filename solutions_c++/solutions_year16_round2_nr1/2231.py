#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{

  int i,j,k,m,n,t;
  scanf("%d",&t);
  for(k=1;k<=t;k++)
  {
    map<char,int> M;
    int arr[10]={0};
    string s;
    cin>>s;

    for(i=0;i<s.length();i++)
    {
    M[s[i]]++;
    }


    if(M['Z'])
    {
      arr[0]+=M['Z'];
      M['E']-=arr[0];
      M['R']-=arr[0];
      M['O']-=arr[0];
      M['Z']-=arr[0];

    }
    if(M['W'])
    {
      arr[2]+=M['W'];
      M['T']-=arr[2];
      M['W']-=arr[2];
      M['O']-=arr[2];
    }
    if(M['X'])
    {
      arr[6]+=M['X'];
      M['S']-=arr[6];
      M['I']-=arr[6];
      M['X']-=arr[6];
    }
    if(M['U'])
    {
      arr[4]+=M['U'];
      M['F']-=arr[4];
      M['O']-=arr[4];
      M['U']-=arr[4];
      M['R']-=arr[4];
    }
    if(M['G'])
    {
      arr[8]+=M['G'];
      M['E']-=arr[8];
      M['I']-=arr[8];
      M['G']-=arr[8];
      M['H']-=arr[8];
      M['T']-=arr[8];
    }
    arr[3]+=M['R'];
    M['E']-=2*M['R'];
    arr[7]+=M['S'];
    M['N']-=M['S'];
    arr[1]+=M['O'];
    M['N']-=M['O'];
    arr[9]+=M['N']/2;

    arr[5]+=M['F'];

  printf("Case #%d: ",k);
  for(i=0;i<=9;i++)
  {
    j=i;
    while(arr[j])
    {
      printf("%d",j);
      arr[j]--;

    }

  }
  printf("\n");
}
  return 0;
}
