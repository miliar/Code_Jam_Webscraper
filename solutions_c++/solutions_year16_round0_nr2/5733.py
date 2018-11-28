#include <cstdio>
#include <algorithm>

static int minimum_maneuvers(char* pancakes); 
static int count_happy_side_up(const char* first, const char* last);
static int determine_how_many_to_flip(const char* first, const char* last);
static void split(char* first, const char* last);

int main() {

  char pancakes[101];

  int test_cases;
  scanf("%d", &test_cases);

  for (int i = 1; i <= test_cases; ++i) {
    scanf("%s", pancakes);
    printf("Case #%d: %d\n", i, minimum_maneuvers(pancakes));
    *pancakes = '\0';
  }

}

int minimum_maneuvers(char* pancakes) {
  bool done = false;
  const int pancakes_count = strlen(pancakes);
  int last = pancakes_count - count_happy_side_up(pancakes, pancakes + pancakes_count);  
  int result = 0;
  while (!done) {
    if (last == 0) {
      done = true;
    } else {
      int how_many_to_flip = determine_how_many_to_flip(pancakes, pancakes + last);
      std::reverse(pancakes, pancakes + how_many_to_flip);
      split(pancakes, pancakes + how_many_to_flip);
      // printf("   %d   %s ", last, pancakes);
      last -= count_happy_side_up(pancakes, pancakes + last);
      // printf(" %d\n", last);
      result++;
    }
    // if (result >= 50) done = true;
  }
  return result;
}

// Count the pancakes with the happy side up, starting the count from the last element [first, last)
int count_happy_side_up(const char* first, const char* last) {
  const char* before_last = last;
  int result = 0;
  do {
    before_last--;
    if (*before_last == '+') {
      result++;
    } else {
      break;
    }
  } while (before_last != first);
  return result;
}

// Determines how many pancakes to flip
int determine_how_many_to_flip(const char* first, const char* last) {
  int result = 0;
  switch (*first) {
  case '+': {
    const char* first_copy = first;
    while (first != last) {
      if (*first == '+') {
        result++;
      } else {
        break;
      }
      first++;
    }
    first = first_copy;
  }
    break;
  case '-':
    result = last - first;
    break;
  }
  return result;
}

void split(char* first, const char* last) {
  char* first_copy = first;
    while (first != last) {
      *first = *first == '+' ? '-' : '+';
      first++;
    }
    first = first_copy;
}

