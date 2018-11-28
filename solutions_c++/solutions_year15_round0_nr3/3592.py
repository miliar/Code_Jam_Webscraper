#include <stdio.h>

int T;
int l,x;

char data[10000];

int sign;

char result;

int flag;

void work()
{
    scanf("%d",&T);getchar();
    for(int k=1;k<=T;++k)
    {
        scanf("%d %d",&l,&x);getchar();
        scanf("%s",data);getchar();
        flag=0;
        result='1';sign=1;
        for(int i=1;i<=x;++i)
        {
            for(int j=0;j<l;++j)
            {
                switch(result){
                case '1':
                {
                    result=data[j];
                }break;
                case 'i':
                {
                    switch(data[j]){
                    case '1':break;
                    case 'i':result='1';sign*=-1;break;
                    case 'j':result='k';break;
                    case 'k':result='j';sign*=-1;break;
                    }
                }break;
                case 'j':
                {
                    switch(data[j]){
                    case '1':break;
                    case 'i':result='k';sign*=-1;break;
                    case 'j':result='1';sign*=-1;break;
                    case 'k':result='i';break;
                    }
                }break;
                case 'k':
                {
                    switch(data[j]){
                    case '1':break;
                    case 'i':result='j';break;
                    case 'j':result='i';sign*=-1;break;
                    case 'k':result='1';sign*=-1;break;
                    }
                }break;
                }
                if(flag==0&&result=='i') {++flag;}
                else if(flag==1&&result=='k') {++flag;}
                //printf("%c %d %d\n",result,sign,flag);

            }
        }
        if(flag==2&&result=='1'&&sign==-1)
        {
            printf("Case #%d: %s\n",k,"YES");
        }
        else
        {
            printf("Case #%d: %s\n",k,"NO");
        }

    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    work();

    fclose(stdin);
    fclose(stdout);

    return 0;
}
