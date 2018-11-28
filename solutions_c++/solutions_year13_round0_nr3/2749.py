#include "iostream"
#include "iomanip"
#include "vector"
#include "numeric"
#include <string>
#include "fstream"
#include "stdlib.h"
#include "algorithm"
#include "math.h"
using namespace std;

string nextHuiwen(string &value);
//数字+1
char addOne(char ch){
    return (ch -'0'+1)%10+'0';
}

string itos(int n){
    string s="";
    while(n){
        s += n%10;
        n=n/10;
    }
    string ret;
    for(string::reverse_iterator itr=s.rbegin();itr!=s.rend();++itr){
        ret.push_back(*itr);
    }
    return ret;
}

bool isHuiwen(const string &str);

int main(){
    string str;
    int n,first,second,tmp;
    fstream ifs("c.in",ios_base::in);
    fstream ofs("c.ou",ios_base::out);
    ifs>>n;
    int counts;
    for(int i=0;i<n;++i){
        ifs>>first>>second;
        counts = 0;
        tmp = sqrt(first);
        if(tmp*tmp<first){
            first = tmp+1;
        }else{
            first = tmp;
        }
        second = sqrt(second);

        for(int j=first;j<=second;++j){
            str = itos(j);
            if(isHuiwen(itos(j))&&isHuiwen(itos(j*j))){
                ++counts;
            }
        }
        ofs<<"Case #"<<i+1<<": "<<counts<<endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}

bool isHuiwen(const string &str){
    bool ret = true;
    string::size_type size = str.size();
    for(string::size_type i=0;i<size/2;++i){
        if(str.at(i)!=str.at(size-1-i)){
            ret = false;
            break;
        }
    }
    return ret;
}

//比n大的下一个回文数
string nextHuiwen(string &value){
    int counts = value.size();
    char* str;
    str = new char[counts+1];
    value.copy(str,counts,0);
    str[counts]=0;
    if(1==counts){
        string nu = "";
        if(str[0]<'9'){
            return ""+addOne(str[0]);
        }else{
            return string("11");
        }
    }

    //现在把str+1
    bool acc = true;
    for(int i=counts-1;i>=0;--i){
        if(acc){
            str[i]=addOne(str[i]);
            if(str[i]!='0'){
                acc=false;
            }
            if(!acc){
                break;
            }
        }
    }


    if(acc){
        string tmp(str);
        tmp = '1'+tmp;
        delete[]str;
        ++counts;
        str = new char[counts+1];
        tmp.copy(str,counts,0);
        str[counts]=0;

    }

   //cout<<"+1\t"<<string(str)<<endl;

    int first = counts/2-1;
    int second = counts/2+1;
    if(counts%2==0){
        --second;
    }
    int finds = -1;
    for(int i=first, j=second;i>=0 && j<counts;--i,++j){
        if(str[i]<str[j]){
            finds = i;
            break;//这个是找到第一个左边比右边小的位置
        }
    }
    //cout<<finds<<endl;
    //把左半边复制给右半边
    for(int i=first, j=second;i>=0 && j<counts;--i,++j){
        str[j]=str[i];
    }
    //左边存在比右边小的，
    if(finds!=-1){
        if(counts%2==0){
            //那么找到的那个位置数字++，赋值给右边对应位置上
            str[finds] = addOne(str[finds]);//既然这个位置小，说明+1不会超过9
            str[second+first-finds] = str[finds];
        }else{
            //奇数位的，那么把中间值++，如果超过9，再把中间两边的++
           char ch = str[second-1] = addOne(str[second-1]);
           int i=first;
            while(ch=='0'){
                ch = str[i]= addOne(str[i]);
                str[second+first-i] = str[i];
            }
        }
    }
    string ret(str);
    delete []str;
    return ret;
}
