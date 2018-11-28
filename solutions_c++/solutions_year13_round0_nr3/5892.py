#include <string.h>
#include <stdio.h>
#include <math.h>

bool checkPalindrome (int num) {
  
  char buffer[512];
  memset(buffer, 0x00, 512);
  sprintf(buffer, "%d", num);

  int len = strlen(buffer);
  int i = 0;
  int j = (len - 1);
  
  while (i <= j) {
    if (buffer[i] != buffer[j])
      return false;

    i++; j--; 
  }

  return true;
}

int main(int argc, char* argv[])
{
  int testCases = 0;
  char lineBuffer[512];

  gets(lineBuffer);
  sscanf(lineBuffer, "%d", &testCases);

  // For each test case.
  for (int testCase = 0; testCase < testCases; testCase++) {
    int numA, numB, numFair = 0;

    gets(lineBuffer);
    sscanf(lineBuffer, "%d %d", &numA, &numB);

    // Reduce search space.
    int numA_sqr = sqrt (numA);
    int numB_sqr = sqrt(numB);

    if (numA_sqr*numA_sqr < numA) 
      numA_sqr++;

    // Test for criteria.
    for (int num = numA_sqr; num <= numB_sqr; num++)
      if (checkPalindrome(num) && checkPalindrome(num*num))
        numFair++;

    // Print results.
    printf("Case #%d: %d\n", testCase+1, numFair);
  }

  return 0;
}

