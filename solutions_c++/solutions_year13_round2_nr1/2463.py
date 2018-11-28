/* 
 * File:   main.cpp
 * Author: metin
 *
 * Created on May 4, 2013, 6:40 PM
 */

#include <cstdlib>
#include <utility>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
using namespace std;

vector<pair<int,int> > arr;
vector<int> line;
int main(int argc, char** argv) {
    
    int start, n;
    int tempnum;
    
    int k;
    cin>>k;
    for(int p=0;p<k;p++){
        
    int count=0;
    line.clear();
    
    cin >> start;
    cin >> n;
    for(int i=0;i<n; i++)
    {
        cin >> tempnum;
        line.push_back(tempnum);
    }
        if(start==1)
    {
        printf("Case #%d: %d\n", p+1,n);
        goto there;
    }
    sort(line.begin(), line.end());
    for(int i=0;i<line.size();i++)
    {
        if(line[i]<start)
        {
            start+=line[i];
        }
        else 
        {
            int copystart=start;
            int localcounter=0;
            for(;;)
            {
                localcounter++;
                copystart=copystart*2-1;
                if(copystart>line[i])
                    break;
                else continue;
            }
            if(line.size()-i <= localcounter)
            {
                printf("Case #%d: %d\n", p+1,count + line.size()-i);
//                cout << count + line.size()-i<<endl;
                goto there;
            }
            else
            {
                start=copystart+line[i];
                count+=localcounter;
            }
        }
    }
    printf("Case #%d: %d\n", p+1,count);
    there :;
    }
//    for(int i=0;i<n;i++)
//    {
//        cin>>tempnum;
//        pair<int,int> temp=make_pair(tempnum,2*tempnum+1);
//        arr.push_back(temp);
//    }
//    
//    for(int i=0; i<arr.size();i++)
//    {
//        cout << "<" << arr[i].first << ", " << arr[i].second<< "> ";
//    }
//    cout << endl;
////    pair<int,int> hold;
//    for(unsigned int i=0;i<arr.size();i++)
//    {
//        here:
//        if(arr[i].second>arr[i+1].first)
//        {
//            arr[i].second+=arr[i+1].first;
//            arr.erase(arr.begin()+i+1);
//            
//            for(int i=0; i<arr.size();i++)
//            {
//                cout << "<" << arr[i].first << ", " << arr[i].second<< "> ";
//            }
//            cout << endl;
//            
//            if(i==arr.size()-1)
//            {
//                break;
//            }
//            goto here;
//        }
//    }
//    for(int i=0; i<arr.size();i++)
//    {
//        cout << "<" << arr[i].first << ", " << arr[i].second<< "> ";
//    }
//    cout << endl;
    return 0;
}

