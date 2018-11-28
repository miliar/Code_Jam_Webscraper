#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <stdlib.h>
#include <string>

using namespace std;
long long int length = 16;
int amount = 50;
//vector<long long int> dividors;
vector<long long int> priems;
vector<string> getValues(vector<string> values){
    //cout << values.size() << endl;
    vector<string> newValues;
    for(string value : values){
        if(!(value.size() >= length-1)){
            newValues.push_back(value+"0");
        }
        newValues.push_back(value+"1");
    }
    if(newValues[0].size() == length){
        return newValues;
    }
    return getValues(newValues);
}

long long int getValueFromBase(long long int base, string value){
    long long int result = 0;
    //cout << base << endl;
    for(int i = 0; i<value.size(); i++){
        //cout << pow(base,((length-i)-1)) << endl;
        if(value[i]=='1'){
            long long int times = 1LL;
            for(int j = 0; j<length-i-1; j++)
                times *= base;
            result += times;
        }
        //cout << result << endl;
    }
    //if(base >= 5)
        //result +=1;
    return result;
}
/*
vector<long long int> getUntil(long long int until){
    for(long long int i = dividors.size(); i <= until; i++){
        long long int toAdd = -1;
        for(long long int j : priems){
            if(i%j == 0){
                toAdd = j;
                break;
            }
            if(j > sqrt(i)){
                break;
            }
        }
        dividors.push_back(toAdd);
        if(toAdd == -1){
            priems.push_back(i);
        }
    }
}*/

vector<long long int> calcPriems(long long int until){
    for(long long int i = 2; i <= until; i++){
        long long int toAdd = 0;
        for(long long int j : priems){
            if(i%j == 0){
                toAdd = j;
                break;
            }
            if(j > sqrt(i)){
                break;
            }
        }
        if(toAdd == 0){
            priems.push_back(i);
            //cout << i << endl;
        }
    }
}

long long int getDivisor(long long int i){
        long long int toAdd = -1;
        for(long long int j : priems){
            if(i%j == 0){
                toAdd = j;
                break;
            }
            if(j > sqrt(i)){
                break;
            }
        }
        if(toAdd == -1){
            priems.push_back(i);
        }
        return toAdd;

}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int i =0; i<T; i++){
        scanf("%lld %d", &length, &amount);
        //dividors.push_back(0);
        //dividors.push_back(0);
        //string t= "1000000000000001";
        //cout << getValueFromBase(9, t) << endl;
        //cout << getValueFromBase(10, t) << endl;
        /*cout << getValueFromBase(3, "1001") << endl;
        cout << getValueFromBase(10, "1001") << endl;
        cout << getValueFromBase(2, "1001") << endl;*/
        //getUntil(10);
        /*for(long long int i=0; i<dividors.size(); i++){
            printf("%lld %lld\n",i, dividors[i]);
        }*/
        //calcPriems(pow(10,(length))/2);
        calcPriems(2000000);
        vector<string> values;
        values.push_back("1");
        values = getValues(values);
        //cout << values.size() << endl;
        //cout << values[0];

        vector<vector<long long int> > solutions;
        for(string value : values){
            //cout << value << endl;
            vector<long long int> solution;
            long long int real=0;
            real = getValueFromBase(10, value);
            //cout << value << endl;
            solution.push_back(real);
            for(int j = 2; j <= 10; j++){
                long long int temp;
                temp = getValueFromBase(j, value);
                //if(temp > dividors.size())
                    //getUntil(temp);
                long long int divisor = getDivisor(temp);
                if(divisor!= -1){
                    solution.push_back(divisor);
                }
                else{
                    break;
                }
                if(j == 10){
                    //cout << "found" << " " << real << endl;
                    solutions.push_back(solution);
                    //cout << "found" << endl;
                }
            }
            if(solutions.size() == amount){
                break;
            }
        }
        printf("Case #%d:\n", i+1);
        for(vector<long long int> solution : solutions){
            for(int j=0; j< (solution.size()-1); j++){
                printf("%lld ", solution[j]);
            }
            printf("%lld\n", solution[solution.size()-1]);
        }
    }

    return 0;
}
