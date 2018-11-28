#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
using namespace std;
int mult[4][4]={{0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
int neorpo[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
char str[100000];
char strlx[100000];
int main()
{
    int T; cin >> T;
    for (int TT = 1 ; TT <= T; TT++)
    {
        int l,x;cin>>l>>x;
        cin>>str;
        int len_str = strlen(str);
        for (int i = 0; i < x; ++i)
        {
            strcpy(strlx+i*len_str,str);  
        }
        //cout<<strlx<<endl;
        int len =strlen(strlx);
        //cout<<len<<endl;
        int ptr = 0;
        int now = 1;
        int tmp = 0;
        int flag = 1;
        int isans = 0;
        for (int i = 0; i < len; ++i)
        {
            while(i<len && tmp != 1)
            {
                //cout<<i<<endl;
                flag *= neorpo[tmp][strlx[i]-'h'];
                tmp  = mult[tmp][strlx[i]-'h'];
                i++;
            }
            if(i==len) break;
            tmp = 0;
            //cout<<i<<endl;
            while(i<len && tmp != 2)
            {
                flag *= neorpo[tmp][strlx[i]-'h'];
                tmp  = mult[tmp][strlx[i]-'h'];
                i++;
            }
            //cout<<i<<endl;
            if(i==len) break;
            tmp = 0;
            while(i<len)
            {
                flag *= neorpo[tmp][strlx[i]-'h'];
                tmp  = mult[tmp][strlx[i]-'h'];
                i++;
            }
            //cout<<flag<<" "<<tmp<<endl;
            if(flag==1 && tmp ==3)
            {
                isans =1;
            }
            break;
        }
        if(isans)
            printf("Case #%d: %s\n",TT,"YES");
        else printf("Case #%d: %s\n",TT,"NO");
    }
    return 0;
}