#include <fstream>
#include <sstream>

int main()
{
    const int TOTAL_COUNT = 4;
    int testCasesCount = 0;
    std::stringstream ss;
    //FILE *pFile = fopen("input.txt", "r");
    //fscanf(pFile, "%d\n", &testCasesCount);
    std::ifstream fin("A-small-attempt0.in");
    std::ofstream fout("output.txt");
    fin >> testCasesCount;
    for(int i = 1; i <= testCasesCount; ++i) {
        const int MAX_LEN = 16;
        char uselessString[MAX_LEN];
        int rowNumA, rowNumB;
        //fscanf(pFile, "%d\n", &rowNumA);
        fin >> rowNumA;
        for(int j = 1; j <= rowNumA; ++j) {
           //fgets(uselessString, MAX_LEN, pFile);
           fin.getline(uselessString, MAX_LEN);
        }
        int rowValuesA[TOTAL_COUNT], rowValuesB[TOTAL_COUNT];
        //fscanf(pFile, "%d %d %d %d\n", &rowValuesA[0], &rowValuesA[1], &rowValuesA[2], &rowValuesA[3]);
        fin >> rowValuesA[0] >> rowValuesA[1] >> rowValuesA[2] >> rowValuesA[3];
        for(int j = rowNumA; j <= TOTAL_COUNT; ++j) {
            //fgets(uselessString, MAX_LEN, pFile);
            fin.getline(uselessString, MAX_LEN);
        }
        //fscanf(pFile, "%d\n", &rowNumB);
        fin >> rowNumB;
        for(int j = 1; j <= rowNumB; ++j) {
            //fgets(uselessString, MAX_LEN, pFile);
            fin.getline(uselessString, MAX_LEN);
        }
        //fscanf(pFile, "%d %d %d %d\n", &rowValuesB[0], &rowValuesB[1], &rowValuesB[2], &rowValuesB[3]);
        fin >>  rowValuesB[0] >> rowValuesB[1] >> rowValuesB[2] >> rowValuesB[3];
        for(int j = rowNumB; j <= TOTAL_COUNT; ++j) {
            //fgets(uselessString, MAX_LEN, pFile);
            fin.getline(uselessString, MAX_LEN);
        }
        int equals = 0;
        int equalVal = 0;
        for (int j = 0; j < TOTAL_COUNT; ++j) {
            for (int k = 0; k < TOTAL_COUNT; ++k) {
                if (rowValuesA[j] == rowValuesB[k]) {
                    ++equals;
                    equalVal = rowValuesA[j];
                }
            }
        }
        ss << "Case #" << i << ": ";
        if (equals > 1) {
            ss << "Bad magician!";
        }
        else if (equals == 1) {
            ss << equalVal;
        }
        else {
            ss << "Volunteer cheated!";
        }
        ss << '\n';
    }
    fin.close();
    fout << ss.str();
    fout.close();
    return 0;
}