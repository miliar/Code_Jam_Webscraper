#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>


using namespace std;


char str[110],flip[110];

bool isCheck(){

    for(int i=0; i<strlen(str); i++){
        if(str[i] == '-')
            return false;
    }

    return true;
}



long getFlip(){
    bool isFlip = false,isCount=true;
    long cnt=0;
    while(!isFlip){
        for(int i=0; i<strlen(str)-1; i++){

            if(str[i] != str[i+1]){

                for(int j=i; j>=0; j--){
                    flip[j] = str[i+1];
                }
                for(int j=0; j<=i; j++){
                    str[j] = flip[i-j];
                }
                cnt++;
            }
        }

        for(int i=0; i<strlen(str); i++){

            if(str[i] == '-'){
                str[i] = '+';
                isCount = false;
            }
        }

        isFlip = isCheck();
    }
    if(isCount)
        return cnt;
    else
        return cnt+1;

}


int main(){


    long t,cs=0;

    scanf("%d",&t);

    while(t--){

        getchar();

        scanf("%s",&str);


        long cnt = getFlip();



        printf("Case #%ld: %ld\n",++cs,cnt);
    }
}
