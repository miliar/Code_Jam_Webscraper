#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#define IsNumber(c) ((char)c >= '0' && (char)c <= '9')

inline int ReadNextInt(char* data, int* dataIndex) {
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

inline void PrintCase(int caseNumber, char* data, int* dataIndex, FILE* outFile) {
  fprintf(outFile, "Case #%d: ", caseNumber+1);

  int length = 0;
  while(data[*dataIndex+length] == '+' || data[*dataIndex+length] == '-') {
    ++length;
  }
  bool* happy = (bool*)malloc(length);

  for(int i = 0; i < length; ++i) {
    happy[i] = data[*dataIndex+i] == '+';
  }

  *dataIndex += length;

  bool allFlipped = false;
  int flipNum = 0;
  while(!allFlipped) {
    allFlipped = true;
    for(int i = 0; i < length; ++i) {
      allFlipped = allFlipped && happy[i];
    }

    if(allFlipped) {
      fprintf(outFile, "%d", flipNum);
      break;
    }

    bool sign = happy[0];
    int p = 1;
    while(p < length && happy[p] == sign) {
      p++;
    }
    for(int i = 0; i < p; ++i) {
      happy[i] = !happy[i];
    }
    ++flipNum;

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
  FILE* inFile = fopen("B-large.in", "r");
  FILE* outFile = fopen("B-large.out", "w");
  if(inFile && outFile) {
    char* data;
    FillBufferWithFile(&data, inFile);
    fclose(inFile);

    int dataIndex = 0;
    int caseCount = ReadNextInt(data, &dataIndex);
    ++dataIndex;

    for(int i = 0; i < caseCount; ++i) {
      PrintCase(i, data, &dataIndex, outFile);
      ++dataIndex;
    }

    fclose(outFile);
  }
}