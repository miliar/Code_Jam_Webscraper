#include <iostream>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
#include <deque>

using namespace std;

int main()
{
    int T=0;
    char arr[1001];
    char arr2[1001];
    int f2=0,l2=0;
    deque<char> d;

    
    scanf("%d",&T);

    for(int i=1;i<=T;i++)
    {
        int re=0;
         scanf("%s", arr);
        int first=1;
        int last =strlen(arr);
        d.push_front(arr[0]);
        for(int j=1;j<strlen(arr);j++)
        {
            char fv =arr[first];
            if(fv >= d.front()){
                d.push_front(fv);
            }else{
                d.push_back(fv);
            }
            first++;

        }
        printf("Case #%d: ",i);
        while(!d.empty()){
            cout << d.front();
            d.pop_front();
        }
        cout << endl;
    }
    return 0;
}
