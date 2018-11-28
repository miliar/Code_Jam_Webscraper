#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;

int get_index(char str[],int &neg_idx){
    int i;
    int posmax=0; 
    for(i=1;str[i];++i){
        if(str[i]=='-'){
           
            neg_idx=i;
        }
        else{
            if(i-1==posmax)
                ++posmax;
        }
            
    }
    return posmax;

}
void reverse(char str[],int l,int r){
    int i;
    //printf("inside reverse\n");
    for(i=l;i<=(r+1)/2;++i){
        
       // printf("str[%d]=%c str[%d]=%c\n",i,str[i],r-i+l,str[r-i+l]);
        

        if(str[i]=='+')
            str[i]='-';
        else
            str[i]='+';
        
        if(i==r-i+l)
            continue;
        if(str[r-i+l]=='+')
            str[r-i+l]='-';
        else
            str[r-i+l]='+';

        char tmp=str[i];
        str[i]=str[r-i+l];
        str[r-i+l]=tmp;
    }
}
int solve(char str[])
{
    int i,neg_idx=-1;
    
    int posmax=get_index(str,neg_idx);
    if(neg_idx!=-1){
        if(posmax==0){
            reverse(str,1,neg_idx);
           // printf("posmax:%s\n",str+1);
           // printf("posmax:%s\n",str+neg_idx);
        }
        else
            for(i=1;i<=posmax;++i)
                str[i]='-';
        
    }
    else 
        return 0;
    
    return 1;   

}
int main()
{
    int t,i;
      
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        //1-based indexing   
        char str[110];
        scanf("%s",str+1);
        int ans=0;
        while(solve(str)){
            ++ans;
        //printf("string:%s\n",str+1);
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
