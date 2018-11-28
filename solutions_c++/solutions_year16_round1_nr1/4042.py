#include<stdio.h>
#include<math.h>
#include<string.h>
#include <vector>

using namespace std;
void TheLastWord(char* FirstWord){
    int length, idx, vec_idx;
    vector<char> newStr;
    
    length = strlen(FirstWord);
    
    for(idx=0; idx<length; idx++){
        //vector<int>::iterator = newStr.begin();
        
        if(idx == 0){
            newStr.push_back(FirstWord[0]);
            continue;
        }else if(newStr[0]>FirstWord[idx]){
            newStr.push_back(FirstWord[idx]);
            continue;
        } else{
            newStr.insert(newStr.begin(),FirstWord[idx]);
        }          
        
    }
    for(vec_idx=0; vec_idx<newStr.size();vec_idx++){
        printf("%c",newStr[vec_idx]);
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
        scanf("%s",str);
        printf("Case #%d: ", cnt+1);
        TheLastWord(str);
        if(cnt!=TestCaseCount-1)
            printf("\n");
    }
    
    fclose(fpIn);
    fclose(fpOut);
    
    return 0;    
}

