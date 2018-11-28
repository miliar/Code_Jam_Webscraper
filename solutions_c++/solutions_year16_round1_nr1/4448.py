#include <iostream>
#include <string.h>

using namespace std;

void the_last(char c[],int size,int pos);
int T;
char out[100][1000];
int lan[100];
int main()
{

    int i=0;
    cin>>T;

    char S[1000];

    for(i=0; i<T; i++)
    {
        cin>>S;
        the_last(S,strlen(S),i);
        lan[i]=strlen(S);

    }


    for(i=0; i<T; i++)
    {
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<lan[i];j++)
        cout<<out[i][j];
        cout<<endl;
    }

    return 0;
}

void the_last(char c[],int size,int pos)
{
    for(int i=0;i<size;i++)
    {
      if(i==0)
        out[pos][0]=c[0];
      if(out[pos][0]>c[i])
      out[pos][i]=c[i];
      else
      {
          for(int j=i;j>=0;j--)
          out[pos][j]=out[pos][j-1];
          out[pos][0]=c[i];
      }

    }

}
