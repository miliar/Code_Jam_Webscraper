#include<iostream>
#include<cstring>
#include<stdio.h>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>
#include<algorithm>

using namespace std;

bool have[10];

bool chafen(int shu){

    int cnt = 0;
    while(shu){
        have[shu%10] = true;
        shu /= 10;
    }
    if(shu)
        have[shu%10] = true;

    for(int i=0 ; i<10 ; i++){
        if(have[i]){
            cnt++;
        }
      //  cout<<"test"<<i<<" = "<<have[i]<<endl;
    }
   // cout<<endl;
    if(cnt==10)
        return true;
    return false;

}

int main()
{
    freopen("A-large.in","r",stdin); //�����ض����������ݽ���in.txt�ļ��ж�ȡ
freopen("out.txt","w",stdout);
    int n,m;
    cin>>n;
    for(int t=1 ; t<=n ; t++){
        cout<<"Case #"<<t<<": ";
        cin>>m;
        if(m==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        int i=2;
        int mm=m;
        memset(have,0,sizeof(have));
        while(!chafen(mm)){
            mm = m*i;
         //   cout<<mm<<" ";
            i++;
        }
       // cout<<endl;
        cout<<mm<<endl;

        //����ض���������ݽ�������out.txt�ļ���
    }
    return 0;
}
