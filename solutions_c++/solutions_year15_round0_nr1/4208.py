#include<fstream>
#include<stdlib.h>

using namespace std ;

int main()
{   ofstream fo;
    fo.open("output.txt");
    ifstream fi;
    fi.open("input.in");
    int T,n,s,out;
    char *c;
    fi>>T;
    for(int i=0;i<T;i++)
    { fi>>n;
      c=(char*)malloc((n+2)*sizeof(char));
      fi>>c;
      s=0; out=0;
      for(int j=0;j<=n;j++)
      { if(j==0)
            s=(c[j]-'0');
        else if(j>s)
		{ out=out+j-s;
          s=(c[j]-'0')+j;
		}
        else
		{ s=s+(c[j]-'0');
		}
       }
      fo<<"Case #"<<i+1<<": "<<out<<endl;
      free(c);
    }
    fo.close();
    fi.close();
    return 0;
}
