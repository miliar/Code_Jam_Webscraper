#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include <vector>
#include <algorithm>

using namespace std;

 struct sort_pred {
        bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
            return left.second > right.second;
         }
    };

bool isPartyMajor(vector<pair<int,int> > senator, int number_of_senators) {
    for(int idx = 0; idx < senator.size(); idx++) {
        if(senator[idx].second > number_of_senators-senator[idx].second) {
            return true;
        }
    }
    return false;
}

void senateEvac() {
    int n, i, number_of_senators;
    char arr[100];
    vector<pair<int,int> > senator;
    number_of_senators = 0;
    scanf("%d",&n);
    for(i = 0; i<n; i++){
        int s;
        scanf("%d",&s);
        pair<int, int> senatorPair;
        number_of_senators += s;
        senatorPair.first = i+1;
        senatorPair.second = s;
        senator.push_back(senatorPair);
    }
    while(number_of_senators != 0) {
        std::sort(senator.begin(), senator.end(), sort_pred());
        senator[0].second -= 1;
        --number_of_senators;
        printf("%c",senator[0].first+64);
        if(number_of_senators == 0) {
            break;
        }
        std::sort(senator.begin(), senator.end(), sort_pred());
        senator[0].second -= 1;
        --number_of_senators; 
        if(isPartyMajor(senator, number_of_senators)) {
            senator[0].second += 1;
            ++number_of_senators;
        } else if(number_of_senators >= 0){
           printf("%c",senator[0].first+64);
        }
        if(number_of_senators != 0)
            printf(" ");
    }
}

int main() {
    int TestCaseCount, cnt;
    char str[200];
    TestCaseCount = 0;
    FILE*   fpIn = freopen("A-large.in", "r+", stdin);
    FILE*   fpOut = freopen("out", "w+", stdout);
    scanf("%d",&TestCaseCount);
    
    for(cnt = 0; cnt<TestCaseCount; cnt++) {
        printf("Case #%d: ", cnt+1);
        senateEvac();
        if(cnt!=TestCaseCount-1)
            printf("\n");
    }
    
    fclose(fpIn);
    fclose(fpOut);
    
    return 0;    
}

