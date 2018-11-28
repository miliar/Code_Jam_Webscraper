#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

static int startSize;
std::vector<int> motes;

int countChanges(int curSize, int numChanges, int curIndex)
{
    // done
    if (curIndex >= motes.size())
        return numChanges;
    
    const int moteSize = motes[curIndex];
    if (curSize > moteSize) {
        return countChanges(curSize+moteSize, numChanges, curIndex+1);
    } else if (curSize > 1) {
        int A = countChanges(curSize+(curSize-1), numChanges+1, curIndex);
        int B = countChanges(curSize, numChanges+1, curIndex+1);
        return std::min(A,B);
    } else {
        return countChanges(curSize, numChanges+1, curIndex+1);
    }
}

bool canSolve()
{
    int curSize = startSize;
    for (int i=0; i<motes.size(); ++i) {
        int mote = motes[i];
        if (mote >= curSize)
            return false;
        curSize += mote;
    }

    return true;
}

int osmos()
{
    std::sort(motes.begin(), motes.end(), [](int a, int b) { return a < b; });
    
    if (canSolve())
        return 0;
    
    return countChanges(startSize, 0, 0);
}

void codeJam(int numcases, FILE* fin, FILE* fout)
{
    for (int test=0; test<numcases; ++test) {
        int numMotes;
        fscanf(fin, "%d%d\n", &startSize, &numMotes);
        
        motes.clear();
        for (int i=0; i<numMotes; ++i) {
            int mote;
            fscanf(fin, "%d ", &mote);
            motes.push_back(mote);
        }
        
        fprintf(fout, "Case #%d: %d\n", test+1, osmos());
    }
}

int main(int argc, const char * argv[])
{
    const char* input = "/Users/malachi/dev/GoogleCodeJam/codejam2013_1B/codejam2013/A-small-attempt0.in";
    const char* output = "/Users/malachi/dev/GoogleCodeJam/codejam2013_1B/codejam2013/A-small-attempt0.out";
    
    FILE* fin = fopen(input, "r");
    if (!fin) {
        printf("unable to open input '%s'\n", input);
        exit(1);
    }
    
    FILE* fout = fopen(output, "w");
    if (!fout) {
        printf("unable to open output '%s'\n", output);
        exit(1);
    }

    int numcases = 0;
    fscanf(fin, "%d\n", &numcases);

    printf("code jamming %d cases: '%s' -> '%s'.\n", numcases, input, output);
    codeJam(numcases, fin, fout);
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}

