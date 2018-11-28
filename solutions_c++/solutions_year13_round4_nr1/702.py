//#include <iostream>
#include <utility>
#include <algorithm>
#include <stack>
#include <fstream>
using namespace std;

ifstream cin("input1.txt");
ofstream cout("output1.txt");

long long cases, stops, events;
pair <long long,long long> event[2000];

long long costOf(long long n){
    return (stops*(stops+1)/2 - (stops-n)*(stops-n+1)/2)%1000002013;
}

bool mySorter (pair <long long,long long> a, pair <long long, long long> b){
    if (a.first != b.first) return a.first < b.first;
    if (a.second != b.second) return a.second > b.second;
    return false;
}

int main(){
    cin>>cases;
    for (long long c = 1; c <= cases; c++){
        long long totalCost = 0;
        cin>>stops>>events;
        for (long long i = 0; i < events; i++){
            cin>>event[i*2].first>>event[i*2+1].first>>event[i*2].second;
            event[i*2+1].second = -event[i*2].second;
            totalCost = (totalCost + event[i*2].second * costOf(event[i*2+1].first - event[i*2].first))%1000002013;
        }
        sort (event, event+events*2, mySorter);
        //for (long long i = 0; i < events*2; i++) cout<<"::"<<event[i].first<<" "<<event[i].second<<"\n";

        long long thisCost = 0;
        stack<pair<long long, long long> > proc;
        for (long long i = 0; i < events*2; i++){
            if (event[i].second > 0) proc.push(event[i]);
            else {
                long long toRemove = -event[i].second;
                while (toRemove > 0){
                    long long removed = min(toRemove, proc.top().second);
                    pair <long long,long long> newOne = proc.top();
                    proc.pop();
                    newOne.second-=removed;
                    thisCost = (thisCost + removed * costOf(event[i].first - newOne.first))%1000002013;
                    toRemove -= removed;

                    if (newOne.second != 0) proc.push(newOne);
                }
            }
        }
        cout <<"Case #"<<c<<": "<<(totalCost-thisCost+1000002013)%1000002013<<"\n";
    }
}
