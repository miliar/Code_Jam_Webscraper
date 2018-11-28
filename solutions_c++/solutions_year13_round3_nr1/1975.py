#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;

std::vector<std::string> pr;
bool isNValThis(std::string word, int nVal)
{   
    bool state = false;
    int count = 0;

    for (int i = 0; i < word.size(); i++) {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') {
            state = false;
            count = 0;
        } else {
            count++;
        }
        if (count == nVal)
            return true;
    }
    return false;
}

int solve(std::string& word, int nVal)
{
    int count = 0, len = 0;
    
    for (int i = 0; i < word.size(); i++) {
        len = 0;
        for (int j = i; j < word.size(); j++) {  
            len++;
            std::string sub_str = word.substr(i, len);
            //pr.push_back(sub_str);
            if (sub_str.size() && isNValThis(sub_str, nVal)) {
                count++;
            }
        }
    }

    return count;
}

int main()
{
    FILE *fp = fopen("prob_small.in", "r");  
    
	int testcase, nVal;
    char word[1000];
    
    fscanf(fp, "%d\n", &testcase);
	for (int caseId = 1; caseId <= testcase; caseId++)
	{               
        fscanf(fp, "%s ", word);
        fscanf(fp, "%d ", &nVal);
       
        int ops = solve(std::string(word), nVal);
        printf("Case #%d: %d\n", caseId, ops);                     

        fscanf(fp, "\n");
	}

	return 0;
}
