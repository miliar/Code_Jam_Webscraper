#include "main.h"

#include <sstream>

using namespace std;

const static size_t kLinesPerTest = 2;

int methodA(const vector<int>& diffs) {
   int total = 0;
   for (size_t i = 0; i < diffs.size(); i++) {
      if (diffs[i] < 0) {
         total += -diffs[i];
      }
   }
   return total;
}

int methodB(const vector<int>& samples, int lowest) {
   int total = 0;
   if (lowest > 0)
      return 0;

   int rate = -lowest;

   TRACE("    " << rate);
   for (size_t i = 0; i < samples.size() - 1; i++) {
      TRACE(" " << min(samples[i], rate));
      total += min(samples[i], rate);
   }
   return total;
}

bool solveTest(
   const vector<string>& lines,
   size_t startingIndex,
   string& result,
   size_t& linesUsed) {

   if (startingIndex + kLinesPerTest > lines.size())
      return false;
   linesUsed = kLinesPerTest;

   size_t numSamples = stoi(lines[startingIndex]);
   vector<int> samples;
   splitAsInt(lines[startingIndex+1], ' ', samples);

   if (samples.size() < 2) {
      result = "0 0";
      return true;
   }

   vector<int> diffs;
   for (size_t i = 0; i < samples.size() - 1; i++) {
      diffs.push_back(samples[i+1] - samples[i]);
   }

   vector<int> sorteddiffs(diffs.begin(), diffs.end());
   sort(sorteddiffs.begin(), sorteddiffs.end());
   int lowest = sorteddiffs[0];

   
   int methodAAnswer = methodA(diffs);
   TRACE(methodAAnswer);
   int methodBAnswer = methodB(samples, lowest);
   TRACE(methodBAnswer);

   stringstream answer;
   answer << methodAAnswer << " "  << methodBAnswer;
   result = answer.str();

   return true;
}