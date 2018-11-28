  #include<iostream>
  #include<cstdio>
  #include<cmath>
  #include<cstdlib>
  #include<cstring>
  #include<algorithm>
  #include<vector>
  #include<stack>
  #include<deque>
  #include<queue>
  #include<utility>
  # define U unsigned long long int
  # define L long long int
  # define INF 2147483648
  using namespace std;
  int main()
  {
      int t;
      cin>>t;
      int a[4],b[4],d1,d2;
      char c[4][4];
      int ir,ic;
      for(int tc=1;tc<=t;tc++)
      {
          int flag=1;
          d1=0,d2=0;
          for(int i=0;i<4;i++)
          {
             a[i]=0;
             b[i]=0;        
          }
          for(int i=0;i<4;i++)
          {
              for(int j=0;j<4;j++)
              {
                  cin>>c[i][j];
                  if(c[i][j]=='T')
                  {
                       ir=i;
                       ic=j;               
                  }
                  if(c[i][j]=='X')
                  {
                     a[i]++;
                     b[j]++;                
                  }
                  else if(c[i][j]=='O')
                  {
                     a[i]--;
                     b[j]--;     
                  } 
                  else if(c[i][j]=='.')flag=0;       
              } 
              if(c[i][i]=='X')d1++;
              else if(c[i][i]=='O')d1--;
              if(c[i][3-i]=='X')d2++;
              else if(c[i][3-i]=='O')d2--;       
          }
          
          if(a[ir]==3)a[ir]++;
          else if(b[ic]==3)b[ic]++;          
          else if(a[ir]==-3)a[ir]--;
          else if(b[ic]==-3)b[ic]--;
          if(d1==3 && ir==ic)d1++;
          else if(d1==-3 && ir==ic)d1--;
          if(d2==3 && (ir+ic)==3)d2++;
          else if(d2==-3 && (ir+ic)==3)d2--;
          sort(a,a+4);
          sort(b,b+4);
          cout<<"Case #"<<tc<<": ";
          if(a[3]==4)cout<<"X won"<<endl;
          else if(b[3]==4)cout<<"X won"<<endl;
          else if(d1==4 || d2==4)cout<<"X won"<<endl;
          else if(d1==-4 || d2==-4)cout<<"O won"<<endl;
          else if(a[0]==-4)cout<<"O won"<<endl;
          else if(b[0]==-4)cout<<"O won"<<endl;
          else if(flag)cout<<"Draw"<<endl;
          else cout<<"Game has not completed"<<endl;
      }
  }
