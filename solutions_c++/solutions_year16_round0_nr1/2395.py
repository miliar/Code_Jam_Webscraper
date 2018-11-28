#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#define IsNumber(c) ((char)c >= '0' && (char)c <= '9')

int ReadNextInt(char* data, int* dataIndex) {
  while(!IsNumber(data[*dataIndex])) {
    ++*dataIndex;
  }

  int startIndex = *dataIndex;
  ++*dataIndex;
  while(IsNumber(data[*dataIndex])) {
    ++*dataIndex;
  }

  int numberLength = *dataIndex - startIndex;
  size_t numberSize = sizeof(char)*numberLength+1;
  char* number = (char*)malloc(numberSize);
  memcpy(number, data+startIndex, numberLength);
  number[numberLength+1] = 0;

  return(atoi(number));
}

inline void PrintCase(int caseNumber, int startNum, FILE* outFile) {
  fprintf(outFile, "Case #%d: ", caseNumber+1);
  if(startNum == 0) {
    fprintf(outFile, "INSOMNIA");
  } else {
    bool numbers[10] = {};
    int currentCountNum = startNum;
    char* countNumStr;
    bool allTen = false;
    int i = 1;

    while(!allTen) {
      currentCountNum = startNum * i;
      _itoa(currentCountNum, countNumStr, 10);

      int j = 0;
      while(countNumStr[j] != 0) {
        numbers[countNumStr[j] - '0'] = true;
        ++j;
      }

      allTen = true;
      for(int k = 0; k < 10; ++k) {
        allTen = allTen && numbers[k];
      }

      ++i;
    }

    fprintf(outFile, "%d", currentCountNum);
  }

  fprintf(outFile, "\n");
}

inline void FillBufferWithFile(char** data, FILE* file) {
  fseek(file, 0, SEEK_END);
  size_t fileSize = ftell(file);
  rewind(file);
  *data = (char *)malloc(fileSize);
  fread(*data, fileSize, 1, file);
}

int main(int argc, const char* argv[]) {

#ifdef SMALL
  char* inFileName = "A-small-attempt0.in";
  char* outFileName = "A-small-attempt0.out";
#endif
#ifdef LARGE
  char* inFileName = "A-large.in";
  char* outFileName = "A-large.out";
#endif

  FILE* inFile = fopen(inFileName, "r");
  FILE* outFile = fopen(outFileName, "w");
  if(inFile && outFile) {

    char* data;
    FillBufferWithFile(&data, inFile);
    fclose(inFile);

    int dataIndex = 0;
    int caseCount = ReadNextInt(data, &dataIndex);

    for(int i = 0; i < caseCount; ++i) {
      int startNum = ReadNextInt(data, &dataIndex);
      PrintCase(i, startNum, outFile);
    }

    fclose(outFile);
  }
}