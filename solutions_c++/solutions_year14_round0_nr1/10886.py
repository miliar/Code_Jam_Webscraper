#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

int main()
{  int casos,c,a,b,algo,num,c1;
    scanf("%d",&casos);
    map<int,int> m;
    int d=1;
    freopen ("out.txt", "w", stdout);
    while(casos--)
    {   scanf("%d",&num);
    m.clear();
        for(a=0;a<4;a++)
        { if (a+1==num)
            { for(b=0;b<4;b++)
    {
                scanf("%d",&algo);
                m[algo]++;
    }
        }
        else
        for(b=0;b<4;b++)
    {
        cin>>algo;
    }

    }
    scanf("%d",&num);
    for(a=0;a<4;a++)
    { if (a+1==num)
    {
        for(b=0;b<4;b++)
    { scanf("%d",&algo);
    m[algo]++;
    }
    }
    else
     {
         for(b=0;b<4;b++)
    { cin>>algo;
    }
     }

    }
   c1=0;
    for(std::map<int,int>::iterator ite=m.begin();ite!=m.end();ite++)
    { if (ite->second==2)
    {
      c1++;
      c=ite->first;
    }
    }
    printf("Case #%d: ",d++);
    if (c1==1 )
    printf("%d\n",c);
    else{
    if (c1==0)
    {
        printf("Volunteer cheated!\n");

    }
    else
    {printf("Bad magician!\n");

    }
    }


    }
    fclose (stdout);

}

