#include <cstdio>
#include<cstring>

using namespace std;

int main(void)
{
    int cases,cas;
    scanf("%d",&cases);

    int len;
    char s[110];
    for(cas=1; cas<=cases;cas++){
        scanf("%s",s);
        len =strlen(s);


        int ans  = 0;
        int beg;
        int end = len-1;

        while(1){
            beg = -1;
            for(;end>=0;end--){
                if(s[end]=='-')
                    break;
            }

            if(end == -1)
                break;

            for(beg = -1;beg+1<len;beg++){
                if(s[beg+1]=='-')
                    break;
            }

            if(beg==-1){
                //ец┤л
                for(int i=0,j=end;i<j;i++,j--){
                    char tmp = s[i];
                    s[i] = s[j];
                    s[j] = tmp;
                }
                for(int i=0;i<=end;i++){
                    if(s[i]=='-'){
                        s[i] ='+';
                    }
                    else{
                        s[i] = '-';
                    }
                }

            }
            else{
                //ец┤л
                for(int i=0,j=beg;i<j;i++,j--){
                    char tmp = s[i];
                    s[i] = s[j];
                    s[j] = tmp;
                }
                for(int i=0;i<=beg;i++){
                    if(s[i]=='-'){
                        s[i] ='+';
                    }
                    else{
                        s[i] = '-';
                    }
                }
            }

            ans++;
        }
        printf("Case #%d: %d\n",cas,ans);

    }

    return 0;
}
