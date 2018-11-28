#include<stdio.h>
#include<list>
using namespace std;
int main()
{
    char str[2000];
    int T,i,j;
    scanf("%d", &T);
    for(i=0;i<T;i++)
    {
        scanf("%s", &str);
        list<char> string;
        list<char>::iterator it;
        it=string.begin();
        it=string.insert(it,str[0]);
        for(j=1;str[j]!=0;j++)
        {
            if(str[j]>=string.front())
            {
                it=string.begin();
            it=string.insert(it,str[j]);
            }
            else
            {
                string.push_back(str[j]);
            }
        }
        printf("Case #%d: ", i+1);
        for (it=string.begin(),j=0; str[j]!='\0'; it++,j++)
        {
            printf("%c",*it);
        }
        printf("\n");

    }
}
