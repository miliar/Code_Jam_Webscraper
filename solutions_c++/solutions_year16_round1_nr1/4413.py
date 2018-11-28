#include <iostream>
#include <string.h>

using namespace std;

void the_last_word(char *c,int size,int num);
int T;
char output[100][1000];
int lan[100];
int main()
{

    int i=0;
    int len;

    cin>>T;

    char S[1000];

    for(i=0; i<T; i++)
    {
        cin>>S;
        len = strlen(S);
        the_last_word(S,len,i);
        lan[i]=len;
    }


    for(i=0; i<T; i++)
    {
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<lan[i];j++)
        cout<<output[i][j];
        cout<<endl;
    }

    return 0;
}

void the_last_word(char *c,int size,int num)
{
    for(int i=0;i<size;i++)
    {
      if(i==0)
        output[num][0]=c[0];
      if(output[num][0]>c[i])
      output[num][i]=c[i];
      else
      {
          for(int j=i;j>=0;j--)
          output[num][j]=output[num][j-1];
          output[num][0]=c[i];
      }

    }

}
