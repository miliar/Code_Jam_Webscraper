#include <stdio.h>
#include <string.h>
int main()
{
    int i,T;
    long long int ans,n,begin,l,end,cur,localMax;
    char name[10000000];
    FILE* ip;
    FILE* op;
    ip = fopen("A-small-attempt1.in","r");
    op = fopen("out.txt","w");
    fscanf(ip,"%d",&T);
    for(i = 1; i <= T; i++) {
        ans = 0;
        fscanf(ip,"%s %I64d",name,&n);
        l = strlen(name);
        for(begin = 0; begin < l; begin++) { //ABR
            end = begin;
            cur = 0;  localMax = 0;
            while( end < l ) { //ABR
                switch( name[end] ) {
                  case 'a':
                  case 'e':
                  case 'i':
                  case 'o':
                  case 'u':
                    cur = 0;
                    break;
                  default:
                    ++cur;
                    localMax = (cur > localMax) ? cur : localMax;
                    break;
                }

                if( localMax >= n ) {
                    ++ans;
                }
                ++end;
            }
        }
        fprintf(op,"Case #%d: %lld\n",i,ans);
    }
    fclose(ip);
    fclose(op);
    return 0;
}
