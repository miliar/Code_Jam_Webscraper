#include <iostream>
#include <set>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <algorithm>
#include <vector>

using namespace std;

bool op_increase (bool i) { return !i; }

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t,gg=1;
    scanf("%d",&t);
    char s[102];
    while(t--)
    {
        vector<bool> foo;
        int count=0;

        scanf("%s",s);

        for(int i=0;s[i]!='\0';i++)
            (s[i]=='-')?foo.push_back(0):foo.push_back(1);

     /*   for (std::vector<bool>::iterator it=foo.begin(); it!=foo.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';*/

      //  cout<<"        "<<*(foo.end()-1)<<"        "<<*foo.begin()<<"      ";

        for (vector<bool>::iterator it=foo.end()-1; it>=foo.begin(); it--)
        {
            //cout<<*it;
            if(*it==0)
            {
                count++;
                vector<bool>::iterator p=foo.begin();
                if(*p==1)
                    count++;

                while(*p==1)
                    p++;

               // if(p-1>=foo.begin())
                {
                    reverse(foo.begin(),p);
                    std::transform (foo.begin(), p, foo.begin(), op_increase);
                }

                reverse(foo.begin(),it+1);
                std::transform (foo.begin(), it+1, foo.begin(), op_increase);
            }
        }
/*
for (std::vector<bool>::iterator it=foo.begin(); it!=foo.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';/*
        int first=0;
        int last=strlen(s)-1;
        int p=last;
        int change=0;
        ///cout<<*change;
        int tmp;
        char sign='-';
        while(first<last)
        {
            while(s[p]!=sign && p<=last && p>=first && first<=last)
            {
                //p--;
                (sign=='-')?p--:p++;
                (sign=='-')?last--:first++;
            }

            if(s[p]==sign)
                count++;

            p=(p==first)?last--:first++;

            sign=(sign=='+')?'-':'+';
/*
            tmp=change;
            change=p;
            p=tmp;
  */
       // }
   //     cout<<count<<endl;
        printf("Case #%d: %d\n",gg++,count);
    }

    return 0;
}
