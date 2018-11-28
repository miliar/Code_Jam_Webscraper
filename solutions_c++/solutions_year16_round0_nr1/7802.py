//
//  main.cpp
//  counting sheep
//
//  Created by zjl on 16/4/9.
//  Copyright © 2016年 zjl. All rights reserved.
//

#include <iostream>

using namespace std;

bool number[10]={false};

int coutingsheep(int num){
    int i = 1;
    int sum = 0;
    while(1){
        sum = i*num;
        int chu = sum;
        while (chu) {
            int yu = chu % 10;
            if(!number[yu])
                number[yu] = true;
            chu = chu/10;
        }
        bool ans = true;
        for(int j = 0; j<10; j++)
            ans = ans && number[j];
        if(ans == true)
            return sum;
        ++i;
    }

}


int main(int argc, const char * argv[]) {

    //freopen("C:\\Desktop\\test.in","r",stdin);
    //freopen("C:\\Desktop\\test.out","w",stdout);

    freopen("C:\\Users\\zjl\\Desktop\\A-large.in","r",stdin);
    freopen("C:\\Users\\zjl\\Desktop\\test.txt","w",stdout);
    int num=0,sums=0;
    scanf("%d",&sums);
    int k =1;
     //数据是从in.txt中输入的
    while(scanf("%d",&num)!=EOF){
        int result = 0;
        //cin>>num;
        if(num == 0)
            cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
            //printf("INSOMNIA");             //写入out.txt中
        else{
            for(int t = 0; t<10; t++)
                number[t]=false;
            result = coutingsheep(num);
            if(result == -1)
                cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
            else
                cout<<"Case #"<<k<<": "<<result<<endl;
        }
        ++k;
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
