#include <iostream>
#include <map>
#include <stdexcept>

#define NUM_QUATERNIONS (4)

#define GET_NEG_QUATS(q1, q2) (q1.isNeg xor q2.isNeg)

struct quaternion {
  quaternion() : quaternion('1', false) {}
  quaternion(char v, bool n) : val(v), isNeg(n) {}
  char val; // 1, i, j, k
  bool isNeg;
};

quaternion multiplyQuaternions(quaternion q1, quaternion q2) {
  if ('1' == q1.val) {
    return quaternion(q2.val, GET_NEG_QUATS(q1, q2));
  } else if ('i' == q1.val) {
    if ('1' == q2.val) {
      return quaternion('i', GET_NEG_QUATS(q1, q2));
    } else if ('i' == q2.val) {
      return quaternion('1', not GET_NEG_QUATS(q1, q2));
    } else if ('j' == q2.val) {
      return quaternion('k', GET_NEG_QUATS(q1, q2));
    } else { // if ('k' == q2.val) {
      return quaternion('j', not GET_NEG_QUATS(q1, q2));
    }
  } else if ('j' == q1.val) {
    if ('1' == q2.val) {
      return quaternion('j', GET_NEG_QUATS(q1, q2));
    } else if ('i' == q2.val) {
      return quaternion('k', not GET_NEG_QUATS(q1, q2));
    } else if ('j' == q2.val) {
      return quaternion('1', not GET_NEG_QUATS(q1, q2));
    } else { // if ('k' == q2.val) {
      return quaternion('i', GET_NEG_QUATS(q1, q2));
    }
  } else { // if ('k' == q1.val) {
    if ('1' == q2.val) {
      return quaternion('k', GET_NEG_QUATS(q1, q2));
    } else if ('i' == q2.val) {
      return quaternion('j', GET_NEG_QUATS(q1, q2));
    } else if ('j' == q2.val) {
      return quaternion('i', not GET_NEG_QUATS(q1, q2));
    } else { // if ('k' == q2.val) {
      return quaternion('1', not GET_NEG_QUATS(q1, q2));
    }
  }
}

std::string displayQuaternion(quaternion q) {
  std::string str;
  str.insert(0, 1, q.val);
  if (q.isNeg) {
    str.insert(0, 1, '-');
  }
  return str;
}

quaternion quaternionFromChar(char c) { return quaternion(c, false); }

#ifdef TEST
void test() {
  char quats[NUM_QUATERNIONS] = {'1', 'i', 'j', 'k'};
  std::cerr << "\t|\t";
  for (size_t i = 0; i < NUM_QUATERNIONS; ++i) {
    std::cerr << quats[i] << "\t|\t";
  }
  std::cerr << std::endl;
  for (size_t i = 0; i < NUM_QUATERNIONS; ++i) {
    std::cerr << quats[i] << "\t|\t";
    for (size_t j = 0; j < NUM_QUATERNIONS; ++j) {
      std::cerr << "__" << displayQuaternion(multiplyQuaternions(
                               quaternionFromChar(quats[i]),
                               quaternionFromChar(quats[j]))) << "__\t|\t";
    }
    std::cerr << std::endl;
  }
}
#endif

// throws std::out_of_range if can't find suitable first index
unsigned long long findFirstIndex(std::string &str, size_t numReps,
                                  unsigned long long fromIndex,
                                  quaternion firstQuat) {
  unsigned long long str_size = str.size();
  for (unsigned long long ind = fromIndex; ind < (str.size() * numReps) - 2;
       ++ind) {
    firstQuat =
        multiplyQuaternions(firstQuat, quaternionFromChar(str[ind % str_size]));
    if ('i' == firstQuat.val and not firstQuat.isNeg) {
      return ind;
    }
  }
  throw std::out_of_range("can't find first index");
}

// throws std::out_of_range if can't find suitable second index
unsigned long long findSecondIndex(std::string &str, size_t numReps,
                                   unsigned long long fromIndex,
                                   quaternion firstQuat) {
  unsigned long long str_size = str.size();
  for (unsigned long long ind = fromIndex; ind < (str.size() * numReps) - 1;
       ++ind) {
    firstQuat =
        multiplyQuaternions(firstQuat, quaternionFromChar(str[ind % str_size]));
    if ('j' == firstQuat.val and not firstQuat.isNeg) {
      return ind;
    }
  }
  throw std::out_of_range("can't find second index");
}

#define FREQ_MEMO (500)

bool checkThirdWorks(std::string &str, size_t numReps,
                     unsigned long long fromIndex, quaternion firstQuat,
                     std::map<unsigned long long, quaternion> &m) {
  unsigned long long str_size = str.size();
  unsigned long long full_str_size = str_size * numReps;
  quaternion curQuat = quaternion();
  unsigned long long distFromEnd;
  unsigned long long closestMemo;
  distFromEnd = full_str_size - fromIndex;
  closestMemo = fromIndex + (distFromEnd % FREQ_MEMO);
  unsigned long long startInd;
  if (distFromEnd > FREQ_MEMO and m.count(closestMemo)) {
    // std::cerr << "!!!!" << std::endl;
    curQuat = m[closestMemo];
    startInd = closestMemo - 1;
  } else {
    startInd = full_str_size - 1;
  }
  for (unsigned long long ind = startInd; ind >= fromIndex; --ind) {
    curQuat =
        multiplyQuaternions(quaternionFromChar(str[ind % str_size]), curQuat);
    // memoize every FREQ_MEMO
    // product of quats from str[ind] -> end of str
    if ((full_str_size - ind) % FREQ_MEMO == 0 and m.count(ind) == 0) {
      // std::cerr << "a;slkdf" << std::endl;
      m[ind] = curQuat;
    }
  }
  firstQuat = multiplyQuaternions(firstQuat, curQuat);
  return ('k' == firstQuat.val and not firstQuat.isNeg);
}

int main() {
  size_t numTestCases;
  size_t numLetters;
  size_t numReps;
  std::string curStr;
  std::cin >> numTestCases;
  bool completed;
  std::map<unsigned long long, quaternion> quatMap;
  for (size_t curCase = 0; curCase < numTestCases; ++curCase) {
    std::cin >> numLetters;
    std::cin >> numReps;
    std::cin >> curStr;
    completed = false;
    quatMap.clear();
    if (curStr.size() != numLetters) {
      throw std::logic_error("cin read the wrong string");
    }
    try {
      unsigned long long firstIndex;
      firstIndex = findFirstIndex(curStr, numReps, 0, quaternion());
      while (!completed) {
        unsigned long long secondIndex;
        secondIndex =
            findSecondIndex(curStr, numReps, firstIndex + 1, quaternion());
        try {
          while (!completed) {
            if (checkThirdWorks(curStr, numReps, secondIndex + 1, quaternion(),
                                quatMap)) {
              // for (std::pair<unsigned long long, quaternion> s : quatMap) {
              //   std::cerr << "ind: " << s.first
              //             << ", quat: " << displayQuaternion(s.second)
              //             << std::endl;
              // }
              std::cout << "Case #" << curCase + 1 << ": YES" << std::endl;
              completed = true;
            } else {
              secondIndex = findSecondIndex(curStr, numReps, secondIndex + 1,
                                            quaternion('j', false));
            }
          }
        } catch (std::out_of_range &) {
          firstIndex = findFirstIndex(curStr, numReps, firstIndex + 1,
                                      quaternion('i', false));
        }
      }
    } catch (std::out_of_range &) { // can't find first index
      std::cout << "Case #" << curCase + 1 << ": NO" << std::endl;
    }
    std::cerr << "DONE WITH CASE #" << curCase + 1 << std::endl;
  }
}
