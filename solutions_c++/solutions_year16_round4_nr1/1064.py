#include<cstdio>
char str[5000];
int n,r,p,s;
int findWinner(){
    int prev[3],arr[3],i,j,k;
    for(i=0;i<3;i++){
        for(j=0;j<3;j++)
            prev[j]=arr[j]=0;
        prev[i]=arr[i]=1;
        for(j=0;j<n;j++){
            for(k=0;k<3;k++){
                arr[(k+1)%3]=arr[(k+1)%3]+prev[k];
            }
            for(k=0;k<3;k++){
                prev[k]=arr[k];
            }
        }
        if(arr[0]==p&&arr[1]==r&&arr[2]==s){
            return i;
        }
    }
    return -1;
}
char get_char(int idx){
    switch(idx){
        case 0:return 'P';
        break;
        case 1:return 'R';
        break;
        case 2:return 'S';
        break;
        default:return ' ';
    }
}
int get_idx(char ch){
    switch(ch){
        case 'P':return 0;
        break;
        case 'R':return 1;
        break;
        case 'S':return 2;
        break;
        default:return -1;
    }
}
void gen_string(int winner){
    str[0]=get_char(winner);
    int i,counter=1,j,k;
    int power=1<<(n-1),inc=1<<(n);
    for(i=1;i<=n;i++){
        j=0;
        while(j<(1<<n)){
            str[power+j]=get_char((get_idx(str[j])+1)%3);
            j+=inc;
        }
        inc=inc>>1;
        power=power>>1;
    }
}
void rearrange(){
    int i,length=2,left,right,j,counter,check;
    char temp;
    str[(1<<n)]='\0';
    for(i=1;i<=n;i++){
        for(j=0;j<(1<<n);j+=length){
            left=j;
            right=j+(length/2);
            counter=0;
            check=0;
            while(counter<length/2){
                if(str[left+counter]<str[right+counter]){
                    check=1;
                    break;
                }
                else if(str[left+counter]>str[right+counter]){
                    check=2;
                    break;
                }
                counter++;
            }
            if(check==2){
                for(counter=0;counter<length/2;counter++){
                    temp=str[left+counter];
                    str[left+counter]=str[right+counter];
                    str[right+counter]=temp;
                }
            }
        }
        length=length*2;
    }
}
int main(){
    int t,i,winner;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d%d%d%d",&n,&r,&p,&s);
        winner=findWinner();
        if(winner==-1)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else{
            gen_string(winner);
            rearrange();
            printf("Case #%d: %s\n",i,str);
        }
    }
    return 0;
}
