#include <bits/stdc++.h>
using namespace std;
class BigNum{
public:
    vector<int> vec;
    BigNum(){}
    BigNum(const char *s, int n){
        vec.clear();
        if(n == 1)
            vec.push_back(s[0]-'0');
        else{
            int en = 0;
            while(s[en] == '0')
                en++;
            for(int i = n-1; i >= en; --i)
                vec.push_back(s[i]-'0');
        }
    }
    void Print(){
        for(int i = vec.size()-1; i >= 0; --i)
            printf("%d", vec[i]);
    }
    bool operator == (const BigNum &other) const{
        if(this->vec.size() != other.vec.size())
            return false;
        for(int i = 0; i < this->vec.size(); ++i)
            if(this->vec[i] != other.vec[i])
                return false;
        return true;
    }
    bool operator < (const BigNum &other) const{
        if(this->vec.size() < other.vec.size()){
            return true;
        }
        else if(this->vec.size() > other.vec.size())
            return false;
        for(int i = this->vec.size()-1; i >= 0; --i){
            if(this->vec[i] != other.vec[i])
                return this->vec[i] < other.vec[i];
        }
        return true;
    }
    bool operator > (const BigNum &other) const{
        if(this->vec.size() > other.vec.size())
            return true;
        else if(this->vec.size() < other.vec.size())
            return false;
        for(int i = this->vec.size()-1; i >= 0; --i){
            if(this->vec[i] != other.vec[i])
                return this->vec[i] > other.vec[i];
        }
        return true;
    }
    BigNum operator + (const BigNum &other) const{
        BigNum tmp;
        for(int i = 0; i < max(this->vec.size(), other.vec.size()); ++i){
            int x = 0;
            if(i < this->vec.size())
                x+=this->vec[i];
            if(i < other.vec.size())
                x+=other.vec[i];
            tmp.vec.push_back(x);
        }
        for(int i = 0; i < tmp.vec.size(); ++i){
            if(tmp.vec[i] >= 10){
                if(i+1 == tmp.vec.size())
                    tmp.vec.push_back(tmp.vec[i]/10);
                else
                    tmp.vec[i+1]+=tmp.vec[i]/10;
                tmp.vec[i]%=10;
            }
        }
        return tmp;
    }
    BigNum operator / (const int &div) const{
        char tmp[this->vec.size()+2];
        int idx = 0, a = 0;
        for(int i = vec.size()-1; i >= 0; --i){
            a*=10;
            a+=vec[i];
            if(a/div > 0){
                tmp[idx] = a/div + '0';
                a-=(a/div)*div;
            }
            else
                tmp[idx] = '0';
            idx++;
        }
        tmp[idx] = NULL;
        return BigNum(tmp, idx);
    }
    BigNum operator * (const int &mul) const{
        BigNum tmp;
        for(int i = 0; i < vec.size(); ++i)
            tmp.vec.push_back(vec[i]*mul);
        for(int i = 0; i < tmp.vec.size(); ++i){
            if(tmp.vec[i] >= 10){
                if(i+1 == tmp.vec.size())
                    tmp.vec.push_back(tmp.vec[i]/10);
                else
                    tmp.vec[i+1]+=tmp.vec[i]/10;
                tmp.vec[i]%=10;
            }
        }
        return tmp;
    }
};
char K[200];
int S;
int C;
int T;
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out small.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%s%d%d",K,&C,&S);
        printf("Case #%d: ",t);
        BigNum k = BigNum(K,strlen(K));
        BigNum hold = BigNum(K,strlen(K));
        for(int i=0;i<C-1;i++){
            hold = hold*S;
        }
        hold = hold/S;
        BigNum temp = BigNum("1",1);
        for(int i=0;i<S;i++){

            temp.Print();
            printf(" ");
            temp = temp + hold;
        }
        printf("\n");


    }
    return 0;
}
